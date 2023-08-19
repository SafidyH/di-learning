from googletrans import Translator

def translate_french_to_english(french_words):
    translator = Translator()
    english_words = {}

    for word in french_words:
        translation = translator.translate(word, src="fr", dest="en")
        english_words[word] = translation.text

    return english_words

# Example usage:
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
english_translations = translate_french_to_english(french_words)
print(english_translations)
