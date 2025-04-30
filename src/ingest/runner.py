import yaml
import os
import sys
from typing import Dict, Any, Optional

class IngestRunner:
    """
    Wrapper class for managing source configuration and invoking ingestion logic.
    """

    def __init__(self, config_path: str = "configs/sources.yaml") -> None:
        """
        Initialize the runner with path to sources.yaml.

        Args:
            config_path (str): Path to the YAML config file.
        """
        self.config_path = config_path
        self.sources = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        Load the YAML configuration file.

        Returns:
            dict: Dictionary of source targets.
        """
        if not os.path.exists(self.config_path):
            print(f"Config file not found: {self.config_path}", file=sys.stderr)
            sys.exit(1)
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def list_targets(self) -> None:
        """
        Print all available source targets with basic info.
        """
        if not self.sources:
            print("No sources found.")
            return

        print("Available targets:\n")
        for name, meta in self.sources.items():
            type_ = meta.get("type", "unknown")
            lang = meta.get("language", "-")
            path = meta.get("path", "-")
            print(f"{name} ({type_}, {lang}) @ {path}")

    def run(self, target_name: str) -> None:
        """
        Run the ingest pipeline for the given target.

        Args:
            target_name (str): Target key in the sources config.
        """
        # Placeholder logic for now
        print(f"[DRY RUN] Would ingest target: {target_name}")
