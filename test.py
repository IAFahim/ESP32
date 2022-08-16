import urequests

x = urequests.request("GET",url="https://iftabcaiiwbjykjgffnp.supabase.co/rest/v1/esp32?username=eq.IAFahim&select=*",
                  headers={'content-type': 'application/json',
                          "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmdGFiY2FpaXdianlramdmZm5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjA2NDIwMDUsImV4cCI6MTk3NjIxODAwNX0.gkcMApVBIh477Q5g47CdzkZXJ2lvlftsEUkTMAN4FsI",
                          "authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmdGFiY2FpaXdianlramdmZm5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjA2NDIwMDUsImV4cCI6MTk3NjIxODAwNX0.gkcMApVBIh477Q5g47CdzkZXJ2lvlftsEUkTMAN4FsI"})
print(x.data)
