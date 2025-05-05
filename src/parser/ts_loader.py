from tree_sitter import Language, Parser
from pathlib import Path

# Add more languages in the future here
PARSER_LIB_PATH = Path("build/my-languages.so")

# Predefined language -> repo mapping
SUPPORTED_LANGUAGES = {
    "python": "tree-sitter-python",
    # "go": "tree-sitter-go",
    # "javascript": "tree-sitter-javascript",
}

LANGUAGE_OBJECTS = {
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
    """
    if language not in LANGUAGE_OBJECTS:
        raise ValueError(f"Unsupported language: {language}")

    parser = Parser()
    parser.set_language(LANGUAGE_OBJECTS[language])
    return parser
