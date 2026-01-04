from fastapi import APIRouter, UploadFile, HTTPException, Depends, BackgroundTasks
from fastapi.responses import FileResponse
from src.domain.entities import File
from src.use_cases.convert_file import ConvertFileUseCase
from src.infrastructure.pillow_converter import PillowConverter
from src.infrastructure.libreoffice_converter import LibreOfficeConverter
import shutil
import os
import asyncio
import tempfile

router = APIRouter()

# Concurrency Control: Limit to 3 concurrent conversions to prevent memory overload (OOM)
# Optimized for t3.micro with 2GB swap
CONVERSION_SEMAPHORE = asyncio.Semaphore(3)

def cleanup_temp_data(temp_dir: str):
    """Cleanup the temporary directory and all its contents."""
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

def get_converter(filename: str):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        return PillowConverter()
    elif ext in ['.doc', '.docx', '.odt']:
        return LibreOfficeConverter()
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported file format: {ext}")

@router.post("/convert")
async def convert_file(file: UploadFile):
    # 1. Save uploaded file to temp
    temp_dir = tempfile.mkdtemp(prefix="pdfhero_")
    temp_path = os.path.join(temp_dir, file.filename)
    
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        source_file = File(
            path=temp_path,
            filename=file.filename,
            format=os.path.splitext(file.filename)[1].lstrip('.'),
            size=os.path.getsize(temp_path)
        )
        
        # 2. Select Converter
        converter = get_converter(file.filename)
        use_case = ConvertFileUseCase(converter)
        
        # 3. Execute with Concurrency Control
        async with CONVERSION_SEMAPHORE:
            result_file = await use_case.execute(source_file, "pdf")
            
        from urllib.parse import quote
        safe_filename = result_file.filename.encode('ascii', 'ignore').decode('ascii') or "converted.pdf"
        encoded_filename = quote(result_file.filename)
        headers = {
            "Content-Disposition": f'attachment; filename="{safe_filename}"; filename*=utf-8\'\'{encoded_filename}'
        }
        
        return FileResponse(
            path=result_file.path, 
            filename=result_file.filename,
            media_type="application/pdf",
            headers=headers
        )

    except Exception as e:
        # Cleanup on failure if we can
        cleanup_temp_data(temp_dir)
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=str(e))
