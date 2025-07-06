import unittest
from src.speech.recognition import SpeechRecognizer
from src.speech.synthesis import TextToSpeech

class TestSpeechFunctions(unittest.TestCase):

    def setUp(self):
        self.recognizer = SpeechRecognizer()
        self.synthesizer = TextToSpeech()

    def test_recognize_speech(self):
        # Assuming recognize_speech() returns a string
        result = self.recognizer.recognize_speech()
        self.assertIsInstance(result, str)

    def test_speak(self):
        text = "Hello, how can I assist you?"
        response = self.synthesizer.speak(text)
        self.assertIsNone(response)  # Assuming speak() returns None

if __name__ == '__main__':
    unittest.main()