from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from src.types.document import Document

class BaseCodeLoader(ABC):
    """
    Abstract base class for code loaders across different programming languages.
    Defines the interface and shared structure for all loader implementations.
    """

    def __init__(self, root_path: str):
        """
        Initialize the loader with a project root path.

        Args:
            root_path (str): The root directory of the code project to ingest.
        """
        self.root_path = Path(root_path)
        self.documents: List[Document] = []

    @abstractmethod
    def load(self) -> List[Document]:
        """
        Subclasses must implement this method to load and return code documents.

        Returns:
            List[Document]: A list of structured documents extracted from the project.
        """
        pass

    def list_code_files(self, extensions: List[str]) -> List[str]:
        """
        Recursively collect all source files under the root path with matching extensions.

        Args:
            extensions (List[str]): File extensions to include (e.g., [".py"]).

        Returns:
            List[str]: Absolute paths of matching source files.
        """
        return [
            str(p.resolve())
            for p in self.root_path.rglob("*")
            if p.is_file() and p.suffix in extensions
        ]