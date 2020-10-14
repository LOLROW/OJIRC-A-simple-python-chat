from scapy.all import *
import os

def connect(roomName, name, ip):
	print("Connecting to " + ip + " in room " + roomName)
	while True:
		msg = input("Message: ")
		msg = roomName + " | " + name + " : " + msg
		try:
			send(IP(dst=ip)/ICMP()/msg)
			os.system("cls")
		except:
			print("Something went wrong...")
			os.system("cls")
def recieve(roomName, host):
	print("Now recieving messages from " + roomName)
	filter_ = "icmp and host " + host
	while True:
		try:
			pkt = sniff(filter=filter_, count = 2)
			message = pkt[0]
			message = str(message)
			indx = message.find(roomName[0])
			msg = message[indx:]
			msg = msg[:-1]
			print(msg)
		except:
			print("Something went wrong...")
def help():
	print("connect(roomName, name, ip) - Sets the room name, your name, and ip.")
	print("recieve(roomName, host)     - Starts recieving messages. \n")
