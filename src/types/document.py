from dataclasses import dataclass

@dataclass
class Document:
    content: str
    metadata: dict  # e.g. {file_path, function_name, start_line}
