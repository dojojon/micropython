
# Based apon https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
 
try:
    import usocket as socket
except:
    import socket
  
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'SKY5C183'
password = 'DXERASAA'

station = network.WLAN(network.STA_IF)

station.active(True)

print('Connecting')
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

def web_page():
    html = """
    <html>
    <head><title>Hello Dojo</title></head>
    <body>
    <h3>Hello from ESP8266</h3>
    <h4>Request Count:
    """ + str(request_count) +"""
    </h4>
    </body>
    </html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a network sockets
s.bind(('', 80)) # bind the local ip address, port 80
s.listen(5) # listen for clients, max connections 5

request_count = 0

while True:
    conn, addr = s.accept()
    request_count += 1
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    response = web_page()
    conn.send(response)
    conn.close()




