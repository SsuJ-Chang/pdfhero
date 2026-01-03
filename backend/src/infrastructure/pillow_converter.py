from src.domain.entities import File
from src.domain.interfaces import FileConverter
from PIL import Image
import os

class PillowConverter(FileConverter):
    """
    Converter implementation using Pillow (PIL) for images.
    Supports formats like JPG, PNG to PDF.
    """
    
    async def convert(self, file: File, target_format: str) -> File:
        if target_format.lower() != "pdf":
            raise ValueError(f"PillowConverter only supports converting to PDF, got {target_format}")
            
        # Determine output path
        output_filename = os.path.splitext(file.filename)[0] + ".pdf"
        output_path = os.path.splitext(file.path)[0] + ".pdf"
        
        # Open image and save as PDF
        # Note: Pillow requires RGB mode for saving as PDF
        with Image.open(file.path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(output_path, "PDF", resolution=100.0)
            
        # Get new file size
        new_size = os.path.getsize(output_path)
        
        return File(
            path=output_path,
            filename=output_filename,
            format="pdf",
            size=new_size,
            content_type="application/pdf"
        )
