from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

#three-way handshaking
clientSocket.connect((serverName, serverPort))
sentence = '{"nome": "Carlos", "cpf": "456456", "numero": 1563}'#input('digite a msg para ser enviada:')

#não precisa indica ip e porta porque isso já foi decidido no estabelecimento de conexão
clientSocket.send(sentence.encode())
receivedSentence = clientSocket.recv(1024)
print('From Server: ', receivedSentence.decode())
clientSocket.close()
