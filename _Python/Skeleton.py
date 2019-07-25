from DB_Commmunication import db_communication

class skeleton:
    def __init__(self):
        self.dbc = db_communication()

    def searchBookbyId(self, bookID):
        book = self.dbc.searchBookbyId(bookID)
        return book

    def searchBookbyName(self, bookName):
        book = self.dbc.searchBookbyName(bookName)
        return book

    def searchClientbyCpf(self, clientCpf):
        client = self.dbc.searchClientbyCpf(clientCpf)
        return client

    def searchClientbyName(self, clientName):
        client = self.dbc.searchClientbyName(clientName)
        return client

    def registerBook(self, title, author, company, edition):
        self.dbc.registerBook(title, author, company, int(edition))
        return 'ok'

    def registerClient(self, cpf, name, phone, adress):
        self.dbc.registerClient(cpf, name, phone, adress)
        return 'ok'

    def removeBook(self, bookID):
        self.dbc.removeBook(bookID)
        return 'ok'

    def removeClient(self, cpf):
        self.dbc.removeClient(cpf)
        return 'ok'
    
    def rentBook(self, bookID, cpf):
        self.dbc.rentBook(bookID, cpf)
        return 'ok'

    def returnBook(self, aluguelID):
        self.dbc.returnBook(int(aluguelID))
        return 'ok'
    def showRented(self):
        rented = self.dbc.showRented()
        reply = ''
        for k in range(0, len(rented), 1):
            reply += str(rented[k])+'@'
        return reply[:-1]