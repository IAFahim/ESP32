import machine
import time
import network
import urequests
import ujson

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


def connect(ssid, password, times=15):
    wifi = network.WLAN(network.STA_IF)
    if wifi.isconnected():
        return wifi
    wifi.active(True)

    networks = wifi.scan()
    print(networks)

    CONNECTION_TIMEOUT_SEC = times

    wifi.connect(ssid, password)

    print("connecting...")
    while (not wifi.isconnected()) and CONNECTION_TIMEOUT_SEC > 0:
        print(times - CONNECTION_TIMEOUT_SEC)
        CONNECTION_TIMEOUT_SEC -= 1
        time.sleep(1)
    if (wifi.isconnected()):
        return wifi


def fetch_data_and_play(wifi, count=10, userName="IAFahim"):
    if wifi.isconnected():
        print("connected going to run 10 times")
        req = 0
        while (req < count):
            x = urequests.request("GET",
                                  url="https://iftabcaiiwbjykjgffnp.supabase.co/rest/v1/esp32?username=eq." + userName + "&select=*",
                                  headers={'content-type': 'application/json',
                                           "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmdGFiY2FpaXdianlramdmZm5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjA2NDIwMDUsImV4cCI6MTk3NjIxODAwNX0.gkcMApVBIh477Q5g47CdzkZXJ2lvlftsEUkTMAN4FsI",
                                           "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmdGFiY2FpaXdianlramdmZm5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjA2NDIwMDUsImV4cCI6MTk3NjIxODAwNX0.gkcMApVBIh477Q5g47CdzkZXJ2lvlftsEUkTMAN4FsI"})
            print(x.text)
            obj = ujson.loads(x.text)
            morseCodeStr = obj[0]["data"]["morseCode"]
            encode_to_morse(morseCodeStr, Led, sound=Sound)
            req += 1
            time.sleep(2)
    else:
        encode_to_morse("SOS", Led, sound=Sound)


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
        print()


Led = machine.Pin(2, mode=machine.Pin.OUT)
Sound = machine.Pin(32, mode=machine.Pin.OUT)

UserName = "IAFahim"
wifi = connect(ssid='HP_LaserZet_2045',password='fahimfahim', times=15)

time.sleep(2)
fetch_data_and_play(wifi, 10, UserName)
