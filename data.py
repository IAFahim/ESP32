import network
import time
import urequests
import ujson

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

networks = wifi.scan()
print(networks)

CONNECTION_TIMEOUT_SEC = 10

wifi.connect('HP_LaserZet_2045', 'fahimfahim')

print("connecting...")
while (not wifi.isconnected()) and CONNECTION_TIMEOUT_SEC < 0:
    print(10 - CONNECTION_TIMEOUT_SEC)
    CONNECTION_TIMEOUT_SEC -= 1
    time.sleep(1000)

if wifi.isconnected():
    print("connected")
    req = 0
    req += 1
    while(req<10):
        x = urequests.request("GET",
                          url="https://iftabcaiiwbjykjgffnp.supabase.co/rest/v1/esp32?username=eq.IAFahim&select=*",
                          headers={'content-type': 'application/json',
                                   "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmdGFiY2FpaXdianlramdmZm5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjA2NDIwMDUsImV4cCI6MTk3NjIxODAwNX0.gkcMApVBIh477Q5g47CdzkZXJ2lvlftsEUkTMAN4FsI",
                                   "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmdGFiY2FpaXdianlramdmZm5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjA2NDIwMDUsImV4cCI6MTk3NjIxODAwNX0.gkcMApVBIh477Q5g47CdzkZXJ2lvlftsEUkTMAN4FsI"})
        print(x.text)
        obj = ujson.loads(x.text)
        morseCode = obj[0]["data"]["morseCode"]


else:
    print("failed")
