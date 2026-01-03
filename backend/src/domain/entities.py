from dataclasses import dataclass
from typing import Optional

@dataclass
class File:
    """
    Represents a file in the system.
    """
    path: str
    filename: str
    format: str
    size: int
    content_type: Optional[str] = None
