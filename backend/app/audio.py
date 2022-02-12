from pathlib import Path

import ffmpeg


class MissingAudioStream(Exception):
    """Raise error if video has no audio stream."""


class FileMissing(Exception):
    """Raise error if file doesn't exist."""


def get_wav(filename: str) -> Path:
    video_path = Path(filename)
    audio_path = Path(f"{video_path.stem}.wav")

    if not video_path.is_file():
        raise FileMissing(f"{filename} doesn't exist")

    # Remove audio file is it exists
    if audio_path.exists():
        audio_path.unlink()

    if not (ffmpeg.probe(filename, select_streams="a")["streams"]):
        raise MissingAudioStream(f"{filename} has no audio stream")

    audio = ffmpeg.input(filename).audio
    stream = ffmpeg.output(audio, str(audio_path))
    ffmpeg.run(stream)

    return audio_path


if __name__ == "__main__":
    print(get_wav("test.mp4"))
