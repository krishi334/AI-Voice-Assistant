import unittest
from src.nlp.processor import NLPProcessor
from src.nlp.intent_classifier import IntentClassifier

class TestNLP(unittest.TestCase):

    def setUp(self):
        self.nlp_processor = NLPProcessor()
        self.intent_classifier = IntentClassifier()

    def test_process_input(self):
        input_text = "Turn on the lights"
        processed_output = self.nlp_processor.process_input(input_text)
        self.assertIsInstance(processed_output, dict)
        self.assertIn('intent', processed_output)

    def test_classify_intent(self):
        input_text = "What's the weather like?"
        intent = self.intent_classifier.classify_intent(input_text)
        self.assertEqual(intent, "get_weather")

    def test_invalid_input(self):
        input_text = ""
        processed_output = self.nlp_processor.process_input(input_text)
        self.assertIsNone(processed_output)

if __name__ == '__main__':
    unittest.main()