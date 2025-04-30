from typing import List, Dict, Any, Optional
from src.loaders import load_code_project

class IngestPipeline:
    """
    IngestPipeline coordinates the ingestion process for a given source.

    It handles loading documents, splitting them into chunks, generating embeddings,
    and building a vector index using the configured backend.
    """

    def __init__(self, config: Dict) -> None:
        """
        Initialize the pipeline with a source configuration.

        Args:
            config (Dict): The target configuration from sources.yaml.
        """
        self.config = config
        self.documents = []
        self.chunks = []
        self.vectors = []

    def run(self) -> None:
        """
        Execute the full ingestion pipeline: load, split, embed, index.
        """
        self.load_documents()
        self.split_documents()
        self.generate_embeddings()
        self.build_index()

    def load_documents(self) -> None:
        """
        Load raw source files and convert them into Document objects.
        Should populate self.documents.
        """
        lang = self.config["language"]
        path = self.config["path"]
        self.documents = load_code_project(path, lang)

    def split_documents(self) -> None:
        """
        Split loaded documents into smaller chunks for embedding.
        Should populate self.chunks.
        """
        raise NotImplementedError

    def generate_embeddings(self) -> None:
        """
        Generate vector embeddings for each chunk using a local model.
        Should populate self.vectors.
        """
        raise NotImplementedError

    def build_index(self) -> None:
        """
        Create a vector index (e.g. FAISS) from the generated embeddings.
        Persist the index to the configured path.
        """
        raise NotImplementedError
