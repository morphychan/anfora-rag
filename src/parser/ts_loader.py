"""
Tree-sitter parser loader module.

This module provides functionality to load and configure Tree-sitter parsers
for different programming languages. It handles the initialization of parsers
and provides a unified interface to access them.
"""

from tree_sitter import Language, Parser
from pathlib import Path
import os
from typing import Dict

# Add more languages in the future here
PARSER_LIB_PATH = Path(__file__).parent / "../build/tree_sitter_parser.so"

# Check if the shared library exists at the specified path
if not os.path.exists(PARSER_LIB_PATH):
    raise FileNotFoundError(f"Tree-sitter library not found at {PARSER_LIB_PATH}")

# Predefined language -> repo mapping
SUPPORTED_LANGUAGES: Dict[str, str] = {
    "python": "tree-sitter-python",
    # "go": "tree-sitter-go",
    # "javascript": "tree-sitter-javascript",
}

# Dictionary mapping language names to their Tree-sitter Language objects
LANGUAGE_OBJECTS: Dict[str, Language] = {
    lang: Language(str(PARSER_LIB_PATH), lang)
    for lang in SUPPORTED_LANGUAGES
}

def get_parser(language: str) -> Parser:
    """
    Return a Tree-sitter parser initialized for the given language.

    Args:
        language (str): Language key, e.g. "python"

    Returns:
        Parser: Configured parser instance

    Raises:
        ValueError: If the specified language is not supported
    """
    if language not in LANGUAGE_OBJECTS:
        error_msg = f"Unsupported language: {language}. Supported languages are: {list(SUPPORTED_LANGUAGES.keys())}"
        raise ValueError(error_msg)

    parser = Parser()
    parser.set_language(LANGUAGE_OBJECTS[language])
    return parser
