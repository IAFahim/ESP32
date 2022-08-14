import network
import time
import urequests

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

networks = wifi.scan()
print(networks)

CONNECTION_TIMEOUT_SEC = 10

wifi.connect('HP_LaserZet_2045', 'fahimfahim')

print("connecting...")
while not wifi.isconnected() and CONNECTION_TIMEOUT_SEC < 0:
    print(10 - CONNECTION_TIMEOUT_SEC)
    CONNECTION_TIMEOUT_SEC -= 1
    time.sleep(1000)

if wifi.isconnected():
    data = urequests.get("https://jsonbase.com/demo_bucket/hello")
    print(data.text)
    print("connected")
else:
    print("failed")

print(wifi.status())