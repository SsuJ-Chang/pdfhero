from src.domain.entities import File
from src.domain.interfaces import FileConverter
import subprocess
import os
import shutil

class LibreOfficeConverter(FileConverter):
    """
    Converter implementation using LibreOffice (headless) for documents.
    Supports formats like DOCX, DOC to PDF.
    """
    
    async def convert(self, file: File, target_format: str) -> File:
        if target_format.lower() != "pdf":
            raise ValueError(f"LibreOfficeConverter only supports converting to PDF, got {target_format}")
            
        # LibreOffice convert-to saves specifically to a directory with original filename + .pdf
        output_dir = os.path.dirname(file.path)
        
        # Construct command
        # --headless: no GUI
        # --convert-to pdf: target format
        # --outdir: output directory
        cmd = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            output_dir,
            file.path
        ]
        
        # Run subprocess
        # Note: This is a blocking call. In a high-concurrency async app, 
        # this should technically be run in an executor (run_in_executor), 
        # but since we use Semaphore to limit total processes, direct call is acceptable for Phase 3 prototype
        # or we can wrap it if needed. For now, strict Semaphore is the key.
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if process.returncode != 0:
             raise RuntimeError(f"LibreOffice conversion failed: {process.stderr.decode()}")
             
        # Determine expected output path
        # LibreOffice replaces extension with .pdf
        output_filename = os.path.splitext(file.filename)[0] + ".pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        if not os.path.exists(output_path):
             raise RuntimeError(f"Conversion succeeded but output file not found at {output_path}")

        new_size = os.path.getsize(output_path)
        
        return File(
            path=output_path,
            filename=output_filename,
            format="pdf",
            size=new_size,
            content_type="application/pdf"
        )
