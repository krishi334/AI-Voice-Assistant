class LanguageSupport:
    def __init__(self):
        self.supported_languages = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'zh': 'Chinese',
            'hi': 'Hindi'
        }

    def translate(self, text, target_language):
        # Placeholder for translation logic
        if target_language not in self.supported_languages:
            raise ValueError(f"Language '{target_language}' is not supported.")
        # Implement translation logic here
        return f"Translated '{text}' to {self.supported_languages[target_language]}"

    def detect_language(self, text):
        # Placeholder for language detection logic
        # Implement language detection logic here
        return 'en'  # Default to English for now

    def get_supported_languages(self):
        return self.supported_languages