import typer

from src.ingest.runner import IngestRunner

app = typer.Typer(help="Ingest code or document into a vector index.")

@app.command("run")
def run(target: str = typer.Option(..., "--target", help="Target name as defined in sources.yaml")):
    """
    Run the ingestion pipeline for a specified source target.

    This command loads the configuration, initializes the pipeline,
    and executes the ingestion process to generate vector indexes.

    Args:
        target (str): Target key as defined in the sources.yaml config file.
    """
    runner = IngestRunner()
    runner.run(target)

@app.command("list")
def list_targets():
    """
    List all available targets defined in the sources.yaml configuration file.
    """
    runner = IngestRunner()
    runner.list_targets()

