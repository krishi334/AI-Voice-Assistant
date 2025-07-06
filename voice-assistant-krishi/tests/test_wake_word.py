import unittest
from src.wake_word.detector import WakeWordDetector

class TestWakeWordDetector(unittest.TestCase):
    def setUp(self):
        self.detector = WakeWordDetector()

    def test_detect_wake_word(self):
        # Simulate audio input for testing
        test_audio = "Hey Krishi, what is the weather today?"
        result = self.detector.detect_wake_word(test_audio)
        self.assertTrue(result)

    def test_ignore_non_wake_word(self):
        # Simulate audio input that does not contain the wake word
        test_audio = "Hello, how are you?"
        result = self.detector.detect_wake_word(test_audio)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()