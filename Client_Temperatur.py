import socket
import sys
import Adafruit_DHT

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.178.185"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))
    
    


while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    send("Temp: {0:0.1f} C Humidity {1:0.1f} %".format(temperature, humidity))
       



send(DISCONNECT_MESSAGE)