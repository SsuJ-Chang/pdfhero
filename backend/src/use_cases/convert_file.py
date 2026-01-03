from src.domain.entities import File
from src.domain.interfaces import FileConverter
import os

class ConvertFileUseCase:
    """
    Use case for converting a file to a target format.
    """
    
    def __init__(self, converter: FileConverter):
        self._converter = converter

    async def execute(self, file: File, target_format: str) -> File:
        """
        Executes the file conversion logic.
        
        Args:
            file: The source file to convert.
            target_format: The desired output format.
            
        Returns:
            File: The converted file entity.
            
        Raises:
            ValueError: If the input file is invalid or target format is not supported (validation logic to be expanded).
        """
        if not file.path:
            raise ValueError("File path cannot be empty")
            
        # Basic validation (can be expanded)
        if file.format == target_format:
            return file

        return await self._converter.convert(file, target_format)
