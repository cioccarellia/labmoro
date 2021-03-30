from socket import *

# Porta del welcome socket.
port = 12000


# Creazione socket TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

binding = ('', port)
serverSocket.bind(binding)


# Mettiamo in attesa di connessioni il welcome socket
serverSocket.listen(1)
print('Il server è in attesa di connessioni')


while True:
    # Passive Open
    connectionSocket, clientAddress = serverSocket.accept()

    print(f'Client {clientAddress}')
    message = connectionSocket.recv(1024).decode('utf-8')

    def do(string):
        return string.upper()

    connectionSocket.send(do(message).encode('utf-8'))


# Welcome = riceve connessione da chiunque client che tentabdi connettersi al server. ogni client verrà gestito dal connection (server)socket. Ci serve rolo per gestir el'apertura della connessionengestita tramite l'accept e il connect.
# Una volta fatto questo ci verrà dato un connectionSocket, che è esclusivo della coppia di socket.
# In udb passavamo sempre l'indirizzo, connectionless. Qui non serve, tutto il traffico routato in quel socket andrà direttamente nella macchina clinet corrispondente.
# Mi spiego meglio. Inizialmente si apre il welcome socket, quando un client richiede una connesione, apro un connection socket con quest'ultimo e lo utilizzo per inviare e ricevere pacchetti.