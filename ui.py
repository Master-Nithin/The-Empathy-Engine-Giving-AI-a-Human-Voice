from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn
from rich.table import Table

console = Console()

def show_header():

    console.print(
        Panel.fit(
            "[bold cyan]Empathy Engine[/bold cyan]\n"
            "AI Emotion-Aware Voice Generator",
            border_style="green"
        )
    )


def show_emotion(emotion, confidence):

    console.print(f"\nDetected Emotion: [bold yellow]{emotion}[/bold yellow]")
    console.print(f"Confidence: {round(confidence,2)}")

    progress = Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%"
    )

    with progress:

        task = progress.add_task("Emotion Intensity", total=100)

        progress.update(task, advance=int(confidence*100))


def show_voice_parameters(params):

    table = Table(title="Voice Parameters")

    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="magenta")

    for k,v in params.items():

        value = str(v)

        table.add_row(k,value)

    console.print(table)