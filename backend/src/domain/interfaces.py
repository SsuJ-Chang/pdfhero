from typing import Protocol
from src.domain.entities import File

class FileConverter(Protocol):
    """
    Interface for file conversion services.
    """
    
    async def convert(self, file: File, target_format: str) -> File:
        """
        Convert a file to the target format.
        
        Args:
            file: The source file to convert.
            target_format: The desired output format (e.g., 'pdf').
            
        Returns:
            File: The converted file entity.
        """
        ...
