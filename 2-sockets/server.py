from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000
binding = ("", SERVER_PORT)

CHARSET = "utf-8"


print("Starting up server at", SERVER_NAME, "over port", SERVER_PORT)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(binding)

print("Socket created.")

while 1:
    print("Listening for messages.")

    buf = 2048
    binaryMessage, clientAddress = serverSocket.recvfrom(buf)
    decodedMessage = binaryMessage.decode(CHARSET)

    print("Recieved message from client", clientAddress[0], "over port", clientAddress[1])
    print("Message content:", decodedMessage)
    print("Processing message")

    def process(message):
        elements = ["a", "e", "i", "o", "u"]
        count = 0
        for it in elements:
            count += message.lower().count(it)
        return len(message) - count


    responseForClient = str(process(decodedMessage))

    print("Sending back message to client.")
    serverSocket.sendto(responseForClient.encode(CHARSET), clientAddress)
    print("Done.\n")


print("Closing Socket")
serverSocket.close()
