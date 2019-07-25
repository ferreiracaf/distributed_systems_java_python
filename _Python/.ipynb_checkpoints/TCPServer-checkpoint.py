from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    #cria o socket pro cliente e estabelece a conexão
    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024)
    
    print(sentence.decode())
    
    connectionSocket.send(sentence)
    
    connectionSocket.close()
