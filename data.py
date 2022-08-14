import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

networks=wifi.scan()
print(networks)

wifi.connect('HP_LaserZet_2045', 'fahimfahim')
print(wifi.isconnected())

