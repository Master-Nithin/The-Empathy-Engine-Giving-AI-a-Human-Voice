from emotion_detector import EmotionDetector
from voice_mapper import VoiceMapper
from tts_engine import TTSEngine
from ui import show_header, show_emotion, show_voice_parameters
from logger import Logger
from rich.console import Console

console = Console()

def get_multiline_input():

    print("\nPaste text (type END to finish):\n")

    lines = []

    while True:

        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return " ".join(lines)


def main():

    show_header()

    detector = EmotionDetector()
    mapper = VoiceMapper()
    tts = TTSEngine()
    logger = Logger()

    while True:

        console.print("\n[bold green]Enter text or type EXIT to quit[/bold green]")

        text = get_multiline_input()

        if text.lower() == "exit":
            break

        emotion, confidence = detector.detect(text)

        show_emotion(emotion, confidence)

        params = mapper.map_voice(emotion, confidence)

        show_voice_parameters(params)

        tts.select_voice(params["gender"])

        tts.set_rate(params["rate"])

        console.print(f"\n[bold cyan]Voice:[/bold cyan] {params['gender']}")

        console.print("[bold blue]Speaking...[/bold blue]\n")

        tts.speak(text)

        logger.log(text, emotion, confidence)


if __name__ == "__main__":
    main()