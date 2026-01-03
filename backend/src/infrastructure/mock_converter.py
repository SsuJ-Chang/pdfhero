from src.domain.entities import File
from src.domain.interfaces import FileConverter
import os

class MockConverter(FileConverter):
    """
    Mock implementation of FileConverter for testing purposes.
    """
    
    async def convert(self, file: File, target_format: str) -> File:
        # Simulate conversion by changing extension and returning a new File object
        # In a real mock, we might not actually create a file on disk unless needed,
        # but here we return a File entity with modified attributes.
        
        new_filename = os.path.splitext(file.filename)[0] + f".{target_format}"
        new_path = os.path.splitext(file.path)[0] + f".{target_format}"
        
        return File(
            path=new_path,
            filename=new_filename,
            format=target_format,
            size=file.size, # Simulate same size or different
            content_type=f"application/{target_format}" # Simplified
        )
