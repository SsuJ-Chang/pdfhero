import pytest
from src.infrastructure.libreoffice_converter import LibreOfficeConverter
from src.domain.entities import File
from unittest.mock import patch, MagicMock
import os
import subprocess

@pytest.mark.asyncio
async def test_libreoffice_convert_command_construction():
    # Arrange
    converter = LibreOfficeConverter()
    input_file = File(
        path="/tmp/doc/test.docx",
        filename="test.docx",
        format="docx",
        size=1000
    )
    
    # We mock subprocess.run and os.path.exists/getsize because we don't want to actually run LO in unit test
    with patch("subprocess.run") as mock_run, \
         patch("os.path.exists") as mock_exists, \
         patch("os.path.getsize") as mock_getsize:
        
        # Mock success
        mock_run.return_value = MagicMock(returncode=0)
        mock_exists.return_value = True
        mock_getsize.return_value = 500
        
        # Act
        result = await converter.convert(input_file, "pdf")
        
        # Assert
        # Check command structure
        mock_run.assert_called_once()
        args = mock_run.call_args[0][0]
        assert args[0] == "soffice"
        assert "--headless" in args
        assert "--convert-to" in args
        assert "pdf" in args
        assert "--outdir" in args
        assert args[-1] == "/tmp/doc/test.docx"
        
        # Check result
        assert result.filename == "test.pdf"
        assert result.path == "/tmp/doc/test.pdf"

@pytest.mark.asyncio
async def test_libreoffice_convert_failure():
    converter = LibreOfficeConverter()
    input_file = File(path="test.docx", filename="test.docx", format="docx", size=100)
    
    with patch("subprocess.run") as mock_run:
        # Mock failure
        mock_run.return_value = MagicMock(returncode=1, stderr=b"Error converting")
        
        # Act & Assert
        with pytest.raises(RuntimeError, match="LibreOffice conversion failed"):
            await converter.convert(input_file, "pdf")
