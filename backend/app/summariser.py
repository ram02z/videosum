from app.audio import get_wav
from app.speech import get_transcript
from spacy import load

spacy_model = load("en_core_web_sm")


def summarise_transcript(
    model,
    transcript: dict[int, str],
    ratio: float = 0.3,
    min_length: int = 60,
    max_length: int = 500,
) -> dict[int, str]:
    text = ""
    for v in transcript.values():
        text += v

    summary = model(text, min_length=min_length)

    doc = spacy_model(summary)

    summarised_timestamps = {}
    for sentence in doc.sents:
        for timestamp, text in transcript.items():
            if str(sentence) in text:
                summarised_timestamps[timestamp] = str(sentence)

    return summarised_timestamps


if __name__ == "__main__":
    from summarizer import Summarizer

    wav_file = get_wav("test.mp4")
    transcript = get_transcript(str(wav_file))
    sum_transcript = summarise_transcript(Summarizer(), transcript)
    print(sum_transcript)
