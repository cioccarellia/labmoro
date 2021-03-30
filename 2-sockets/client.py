from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000
binding = (SERVER_NAME, SERVER_PORT)

CHARSET = "utf-8"

print("Connecting to", SERVER_NAME, "over port", SERVER_PORT)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)

while True:
    message = input(">>: ")
    clientSocket.sendto(message.encode(CHARSET), binding)

    try:
        buf = 2048
        binaryMessage, serverAddress = clientSocket.recvfrom(buf)

        decodedMessage = binaryMessage.decode(CHARSET)
        print("<<:", decodedMessage)
    except:
        print("--|")

print("Closing Socket")
clientSocket.close()
