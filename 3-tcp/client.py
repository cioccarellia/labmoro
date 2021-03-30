from socket import *

serverName = 'localhost'
serverPort = 12000


# Creazione socket TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connessione al welcome socket
clientSocket.connect((serverName, serverPort))


message = input('Numero: ').encode('utf-8')


# Non serve specificare a chi si manda. è ovvio.
clientSocket.send(message)


# 1024 è la dimensione non del buffer a livello TCP ma a livello applicativo
modifiedMessage = clientSocket.recv(1024)
print(f'Dal server: {modifiedMessage.decode("utf-8")}')

clientSocket.close()