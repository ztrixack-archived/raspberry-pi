CODE = {
    'A': '.-',      'B': '-...',    'C': '-.-.',
    'D': '-..',     'E': '.',       'F': '..-.',
    'G': '--.',     'H': '....',    'I': '..',
    'J': '.---',    'K': '-.-',     'L': '.-..',
    'M': '--',      'N': '-.',      'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',
    'S': '...',     'T': '-',       'U': '..-',
    'V': '...-',    'W': '.--',     'X': '-..-',
    'Y': '-.--',    'Z': '--..',

    '0': '-----',   '1': '.----',   '2': '..---',
    '3': '...--',   '4': '....-',   '5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',
    '9': '----.',

    '.': '.-.-.-',  ',': '--..--',  '?': '..--..',
    '`': '.----.',  '!': '-.-.--',  '/': '-..-.',
    '(': '-.--.',   ')': '-.--.-',  '&': '.-...',
    ':': '---...',  ';': '-.-.-.',  '=': '-...-',
    '+': '.-.-.',   '-': '-....-',  '_': '..--.-',
    '"': '.-..-.',  '$': '...-..-', '@': '.--.-.'
    }

CODE_REVERSED = {value:key for key,value in CODE.items()}

DASH = '-'
DOT = '.'

def encode(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def decode(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())
