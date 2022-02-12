import os
import time

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()
AZURE_KEY = os.getenv("AZURE_KEY")


def get_transcript(filename: str):
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_KEY, region="uksouth")
    speech_config.request_word_level_timestamps()
    speech_config.enable_dictation()
    audio_input = speechsdk.AudioConfig(filename=filename)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input
    )

    done = False

    def stop_cb(event):
        print(f"CLOSING on {event}")
        nonlocal done
        done = True

    transcript = {}

    def main_handler(event):
        print(f"offset: {event.result.offset}, text: {event.result.text}")
        transcript[event.result.offset] = event.result.text

    speech_recognizer.recognized.connect(main_handler)

    speech_recognizer.session_started.connect(
        lambda event: print(f"SESSION STARTED: {event}")
    )
    speech_recognizer.session_stopped.connect(
        lambda event: print(f"SESSION STOPPED: {event}")
    )

    speech_recognizer.canceled.connect(stop_cb)
    speech_recognizer.session_stopped.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(0.5)

    speech_recognizer.stop_continuous_recognition()
    return transcript


if __name__ == "__main__":
    r = get_transcript("test.wav")
    from pprint import pprint

    pprint(r)
