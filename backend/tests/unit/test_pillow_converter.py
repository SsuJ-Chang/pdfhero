import pytest
from src.infrastructure.pillow_converter import PillowConverter
from src.domain.entities import File
from PIL import Image
import os
import tempfile

@pytest.mark.asyncio
async def test_pillow_convert_success():
    # Arrange
    converter = PillowConverter()
    
    # Create a dummy image
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        img = Image.new('RGB', (60, 30), color = 'red')
        img.save(tmp, format='PNG')
        tmp_path = tmp.name
        
    input_file = File(
        path=tmp_path,
        filename="test.png",
        format="png",
        size=os.path.getsize(tmp_path)
    )
    
    try:
        # Act
        result = await converter.convert(input_file, "pdf")
        
        # Assert
        assert result.format == "pdf"
        assert result.filename == "test.pdf"
        assert os.path.exists(result.path)
        
        # Verify it is a valid PDF (basic check)
        with open(result.path, "rb") as f:
            header = f.read(4)
            assert header == b"%PDF"
            
    finally:
        # Cleanup
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        if 'result' in locals() and os.path.exists(result.path):
            os.remove(result.path)

@pytest.mark.asyncio
async def test_pillow_convert_invalid_format():
    converter = PillowConverter()
    input_file = File(path="test.txt", filename="test.txt", format="txt", size=0)
    
    # Act & Assert
    with pytest.raises(ValueError, match="only supports converting to PDF"):
        await converter.convert(input_file, "docx")
