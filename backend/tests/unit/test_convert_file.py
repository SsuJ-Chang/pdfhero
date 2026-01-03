import pytest
import asyncio
from src.domain.entities import File
from src.use_cases.convert_file import ConvertFileUseCase
from src.infrastructure.mock_converter import MockConverter

@pytest.mark.asyncio
async def test_convert_file_success():
    # Arrange
    converter = MockConverter()
    use_case = ConvertFileUseCase(converter)
    
    input_file = File(
        path="/tmp/test.docx",
        filename="test.docx",
        format="docx",
        size=1024
    )
    target_format = "pdf"
    
    # Act
    result = await use_case.execute(input_file, target_format)
    
    # Assert
    assert result.filename == "test.pdf"
    assert result.format == "pdf"
    assert result.path == "/tmp/test.pdf"

@pytest.mark.asyncio
async def test_convert_file_same_format():
    # Arrange
    converter = MockConverter()
    use_case = ConvertFileUseCase(converter)
    
    input_file = File(
        path="/tmp/test.pdf",
        filename="test.pdf",
        format="pdf",
        size=1024
    )
    target_format = "pdf"
    
    # Act
    result = await use_case.execute(input_file, target_format)
    
    # Assert
    assert result == input_file # Should return the same object without conversion

@pytest.mark.asyncio
async def test_convert_file_empty_path():
    # Arrange
    converter = MockConverter()
    use_case = ConvertFileUseCase(converter)
    
    input_file = File(
        path="",
        filename="test.docx",
        format="docx",
        size=1024
    )
    
    # Act & Assert
    with pytest.raises(ValueError, match="path cannot be empty"):
        await use_case.execute(input_file, "pdf")
