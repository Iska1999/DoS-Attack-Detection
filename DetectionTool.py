from scapy.all import*
import socket
import time
from struct import *
import netifaces as nif
from datetime import datetime

def DeviceScan(target_ip):
    #Network scan code courtesy of https://www.thepythoncode.com/article/building-network-scanner-using-scapy
    # IP Address for the destination
    # create ARP packet
    arp = ARP(pdst=target_ip)
    # create the Ether broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp #stack the packet
    result = srp(packet, timeout=3, verbose=False)[0] #send the packet and receive another containing the result
    
    devices = [] #Contains the device(s) corresponding to the target IP
    devices_dict ={} #will be used for later on
    for sent, received in result:
        # for each reply, append ip and mac address to 'devices' list
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        devices_dict[received.psrc] = received.hwsrc
    # print devices
    print("Devices of the network:")
    print("IP" + " "*18+"MAC")
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))
    return devices_dict    
def ServerCode(Host,Port,devices_dict):
    #The dictionary idea was inspired by :https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_dos_and_ddos_attack.htm
    #Two thresholds (alert and threshold) was my idea, The values are arbitrary
    IP_list = {} #Dictionary with recent IPs.Takes IP as key and returns number of connections (hit) as value
    Alert = 15
    Threshold = 35
    #I learned socket programming basics from https://realpython.com/python-sockets/
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('', Port))
    print('Connection successful!')
    seconds=time.time()
    while True:
        s.listen()
        print("Listening for connections...")
        conn, addr = s.accept()
        IP_addr=addr[0]
        if IP_addr in IP_list:
            IP_list[IP_addr]=IP_list[IP_addr]+1
        else:
            print("New connection from",IP_addr)
            IP_list[IP_addr]=1 #new entry, only 1 hit
        if ((IP_list[IP_addr]>=Alert) and (IP_list[IP_addr]<Threshold) ): #Alert is only used to bring attention to a potential attack
            print("Number of connections from",IP_addr,":",IP_list[IP_addr])
            print("Potential DDoS Attack from:",IP_addr)
        if (IP_list[IP_addr]>=Threshold):
            print("Number of connections from",IP_addr,":",IP_list[IP_addr])            
            print("Confirmed DDoS attack from ",IP_addr)
            if (IP_addr in devices_dict) or (IP_addr =='127.0.0.1'): #The other condition is for testing purposes -- you probably won't attack yourself
                print("Attacker's IP is from within the network")
            #return
        #I decided to flush the recent IPs every x (in this case 5) seconds since 35 connections for a day or week don't account for a DDoS. 
        #They must be sent in a short duration
        if (time.time()-seconds>=5):
            seconds=time.time()
            print("Flushing recent IP connections list...")
            IP_list.clear()       
Host = '127.0.0.1'  
Port = 80 #In this case we attack the HTTP server
devices_dict={}       
devices_dict=DeviceScan("192.168.1.1/24")
#I decided to do a network scan to find all IPs on my network
#Upon detecting a DDos attack, I compare the attacker IP with the devices in my network to see if the IP is from within the network
#Yes, the IP could be spoofed but this at least provides a first step in identifying and tracking the attacker
#We could then compare MAC addresses of the attacker and the IP of the device in the network, for example.
ServerCode(Host,Port,devices_dict)

