import machine
import time

morseAlphabet = {
    "E": ".",
    "T": "-",

    "I": "..",
    "A": ".-",
    "N": "-.",

    "M": "--",
    "S": "...",
    "U": "..-",
    "R": ".-.",

    "W": ".--",
    "D": "-..",

    "K": "-.-",
    "G": "--.",
    "O": "---",

    "H": "....",
    "V": "...-",
    "F": "..-.",

    "L": ".-..",

    "P": ".--.",
    "J": ".---",

    "B": "-...",
    "X": "-..-",

    "C": "-.-.",
    "Y": "-.--",
    "Z": "--..",
    "Q": "--.-",

    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",

    " ": "/",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "=": "-...-"
}


def encode_to_morse(message, led, sound):
    for char in message[:]:
        for c in morseAlphabet[char.upper()]:
            print(c)
            if c == '-':
                led.on()
                sound.on()
                time.sleep_ms(300)
                led.off()
                sound.off()
                time.sleep_ms(300)
            elif c == '/':
                time.sleep_ms(700)
            else:
                led.on()
                sound.on()
                time.sleep_ms(100)
                led.off()
                sound.off()
                time.sleep_ms(300)


Led = machine.Pin(2, mode=machine.Pin.OUT)
Sound = machine.Pin(32, mode=machine.Pin.OUT)

encode_to_morse("ET IAN MSUR WD KGO HVF L PJ BX CYZQ 1234567890", Led, sound=Sound)
