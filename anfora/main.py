import typer
from anfora.cli import ingest

class AnforaCLI:
    """
    Main CLI entry point for the Anfora RAG system.
    """

    def __init__(self):
        """
        Initialize the CLI application and register available subcommands.
        """
        self.app = typer.Typer(help="Anfora: A local RAG system for code and document ingestion.")
        self._register_commands()

    def _register_commands(self):
        """
        Register all subcommands (e.g., ingest, chat) to the main CLI app.
        """
        self.app.add_typer(ingest.app, name="ingest", help="Ingest code or document into a vector index")
        # Future subcommands:
        # self.app.add_typer(chat.app, name="chat")
        # self.app.command()(self.list_targets)

    def run(self):
        """
        Execute the CLI application.
        """
        self.app()

if __name__ == "__main__":
    AnforaCLI().run()