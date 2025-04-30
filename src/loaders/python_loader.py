from typing import List
from src.loaders.base_loader import BaseCodeLoader
from src.types.document import Document

class PythonCodeLoader(BaseCodeLoader):
    """
    Loads a Python codebase and extracts semantic code units (functions, classes).
    """
    def __init__(self, root_path: str):
        super().__init__(root_path)
        self.documents = []

    def load(self) -> List[Document]:
        """
        Walk the project directory, parse .py files, and extract structured code chunks.

        Returns:
            List[Document]: Extracted function and class code blocks with metadata.
        """
        source_files = self.list_code_files([".py"])

        for path in source_files:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    source_code = f.read()
                # Placeholder for AST-based extraction (to be implemented)
                # self.documents.extend(self._extract_documents(path, source_code))
                print(f"Loaded file: {path} (size: {len(source_code)} chars)")
            except Exception as e:
                print(f"Failed to read file: {path} — {e}")

        return self.documents

def load_python_project(path: str) -> List[Document]:
    """
    Adapter function for loading a Python project.

    Args:
        path (str): Path to the Python project.

    Returns:
        List[Document]: List of extracted documents.
    """
    return PythonCodeLoader(path).load()