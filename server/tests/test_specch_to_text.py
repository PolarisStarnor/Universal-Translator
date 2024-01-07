import unittest
import pathlib
import speech_to_text
import warnings

class TestAudioToText(unittest.TestCase):

    def test_audio_input(self):
        file: pathlib.Path = pathlib.Path('tests/test_audio/this_is_a_test_recording.mp3')
        transcription: str = speech_to_text.transcribe(file)

        self.assertIn("this is a test recording", transcription.lower())
        if (transcription.lower() != "this is a test recording"):
            warnings.warn("The sequences are not exactly equal:\n    Transcription raw output: " + transcription)

    def test_long_audio(self):
        file: pathlib.Path = pathlib.Path('tests/test_audio/convoluded.mp3')
        transcription: str = speech_to_text.transcribe(file)

        self.assertIn("this is a convoluted example", transcription.lower())


if __name__ == '__main__':
    unittest.main()
