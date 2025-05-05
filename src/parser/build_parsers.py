# scripts/build_parsers.py
from tree_sitter import Language
from pathlib import Path

if __name__ == "__main__":
    output_path = Path("build/languages.so")
    print(f"[Tree-sitter] Building parsers...")

    Language.build_library(
        str(output_path),  # Output path
        [
        "vendor/tree-sitter-python",
        # Add more languages here
        ]
    )

    print(f"[Tree-sitter] Build complete: {output_path}")