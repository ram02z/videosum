from app.audio import get_wav
from app.speech import get_transcript


def summarise_transcript(model, transcript: dict[int, str]) -> dict[int, str]:
    for k, v in transcript.items():
        text = "".join(v)
        transcript[k] = model(text)

    return transcript


if __name__ == "__main__":
    from summarizer import Summarizer

    wav_file = get_wav("test.mp4")
    transcript = get_transcript(str(wav_file))
    sum_transcript = summarise_transcript(Summarizer(), transcript)

    for k, v in sum_transcript.items():
        print(k)
        print(v)
