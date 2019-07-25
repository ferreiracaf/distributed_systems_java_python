import json
from Skeleton import skeleton

# TRATA A MENSAGEM DO SERVIDOR 

class dispatcher:
    def __init__(self):
        self.skl = skeleton()

    def invoke(self, message):
        flag = 0
        strMessage = str(message)
        if strMessage[0] != '{':
            flag = 1
            strMessage = message[2:]
            strJava = message[:1]
        
        messageDict = json.loads(strMessage)
        
        #logica de escolher as opcoes aqui

        # Service SEARCH
        if messageDict['objectReference'] == 'search':
            if messageDict['methodName'] == 'bookID':
                bookID = messageDict['arguments']
                args = self.skl.searchBookbyId(bookID)
                args = str(args).replace('(', '')
                args = str(args).replace(')', '')
                args = str(args).replace('\'', '')

            elif messageDict['methodName'] == 'bookName':
                bookName = messageDict['arguments']
                args = self.skl.searchBookbyName(bookName)
                args = str(args).replace('(', '')
                args = str(args).replace(')', '')
                args = str(args).replace('\'', '')

            elif messageDict['methodName'] == 'clientCpf':
                cpf = messageDict['arguments']
                args = self.skl.searchClientbyCpf(cpf)
                args = str(args).replace('(', '')
                args = str(args).replace(')', '')
                args = str(args).replace('\'', '')

            elif messageDict['methodName'] == 'clientName':
                clientName = messageDict['arguments']
                args = self.skl.searchClientbyName(clientName)
                args = str(args).replace('(', '')
                args = str(args).replace(')', '')
                args = str(args).replace('\'', '')

        # Service REGISTER
        elif messageDict['objectReference'] == 'register':
            if messageDict['methodName'] == 'book':
                args = str(messageDict['arguments']).split(';')
                title = args[0]
                author = args[1]
                company = args[2]
                edition = args[3]
                args = self.skl.registerBook(title, author, company, edition)
            
            elif messageDict['methodName'] == 'client':
                args = str(messageDict['arguments']).split(';')
                cpf = args[0]
                name = args[1]
                phone = args[2]
                adress = args[3]
                args = self.skl.registerClient(cpf, name, phone, adress)

        # Service REMOVE
        elif messageDict['objectReference'] == 'remove':
            if messageDict['methodName'] == 'book':
                bookID = messageDict['arguments']
                args = self.skl.removeBook(bookID)

            elif messageDict['methodName'] == 'client':
                cpf = messageDict['arguments']
                args = self.skl.removeClient(cpf)
        
        # Service LIB
        elif messageDict['objectReference'] == 'lib':
            if messageDict['methodName'] == 'rent':
                args = str(messageDict['arguments']).split(';')
                bookID = args[0]
                cpf = args[1]
                args = self.skl.rentBook(bookID, cpf)

            elif messageDict['methodName'] == 'return':
                aluguelID = messageDict['arguments']
                args = self.skl.returnBook(aluguelID)

            elif messageDict['methodName'] == 'rented':
                args = self.skl.showRented()
                args = str(args).replace('datetime.date', '')
                # args = str(args).replace(')),(', '))@(')

        # organizar as respostas
        messageDict['type'] = 1
        messageDict['arguments'] = str(args)

        reply = json.dumps(messageDict)
        reply = reply.replace(': ', ':')
        reply = reply.replace(', ', ',')
        if flag == 1:
            tam = len(reply)
            strJava += chr(tam)
            reply = strJava+reply
        return reply, tam


        