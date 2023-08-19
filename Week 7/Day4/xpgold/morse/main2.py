MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/',
}

def text_to_morse(english_text):
    english_text = english_text.upper() #transforme en msjuscule
    morse_code = []

    for char in english_text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')

    return ' '.join(morse_code)

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    english_text = []

    for code in morse_code:
        for letter, morse in MORSE_CODE_DICT.items():
            if morse == code:
                english_text.append(letter)
                break
        else:
            english_text.append(' ')

    return ''.join(english_text)

if __name__ == "__main__":
    english_text = input("Enter English text: ")
    morse_code = text_to_morse(english_text)
    print(f"Morse Code: {morse_code}")

    morse_input = input("Enter Morse code: ")
    english_text = morse_to_text(morse_input)
    print(f"English Text: {english_text}")
