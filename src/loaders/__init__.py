from typing import List

from src.types.document import Document
from .python_loader import PythonCodeLoader

def load_code_project(path: str, language: str) -> List[Document]:
    """
    Load code project files into structured documents.
    
    Args:
        path (str): Path to the code project root.
        language (str): Programming language ("python", "js", etc.)
    
    Returns:
        List[Document]: List of parsed documents.
    """
    if language == "python":
        loader = PythonCodeLoader(path)
        return loader.load()
    raise ValueError(f"Unsupported language: {language}")
