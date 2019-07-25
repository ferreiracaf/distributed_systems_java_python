import socket
from Dispatcher import dispatcher

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
disp = dispatcher()

def getRequest():
    sentence = connectionSocket.recv(1024)
    strMessage = sentence.decode()    
    return strMessage

def sendResponse(message):
    reply = str(message).encode()
    connectionSocket.send(reply)

print('The server is ready to receive')
while True:
    #cria o socket pro cliente e estabelece a conexão
    connectionSocket, addr = serverSocket.accept()

    message = getRequest()

    print(message)
    print('\t-----')
    
    reply, tam = disp.invoke(message)

    if tam > 126:
        resp1 = reply[2:126]
        tam1 = len(resp1)
        header1 = reply[0]+chr(tam1)
        resp1 = header1+resp1
        sendResponse(resp1)
          
        resp2 = reply[126:]
        # while len(resp2) < 42:
        #     resp2 += '!'
        tam2 = len(resp2)
        header2 = reply[0]+chr(tam2)
        resp2 = header2+resp2
        sendResponse(resp2)
        print(type(resp1+resp2), resp1+resp2)
        print(tam, tam2)
        print("\t##### ")
    else:
        sendResponse(reply)
        print(type(reply), reply)
        print(tam)
        print("\t##### ")

    connectionSocket.close()