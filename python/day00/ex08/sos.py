import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----'}

del sys.argv[0]
text = ' '
text = (text.join(sys.argv)).upper()

morsetext = ''
for c in text:
    if c in MORSE_CODE_DICT:
        morsetext += MORSE_CODE_DICT[c]
    elif c == ' ':
        morsetext += '/'
    else:
        print("ERROR")
        sys.exit()
    morsetext += ' '
print(morsetext[:-1])
