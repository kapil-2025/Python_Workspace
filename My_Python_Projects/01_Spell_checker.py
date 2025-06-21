from spellchecker import SpellChecker

class SpellCheckerApps:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()  # hello world → ['hello', 'world']
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)  # join with space

    def run(self):
        print("\n--- Spell Checker ---")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')
            if text.lower() == 'exit':
                print('Closing the program...')
                break
            corrected_text = self.correct_text(text)
            print(f'Corrected text: {corrected_text}')

# This must be outside the class
if __name__ == "__main__":
    SpellCheckerApps().run()
