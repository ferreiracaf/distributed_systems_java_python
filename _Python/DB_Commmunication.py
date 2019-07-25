import psycopg2 as pg2
import datetime

class db_communication:

    def __init__(self):
        self.conn = pg2.connect( user = "postgres",
                    password = "159789",
                    host = "127.0.0.1",
                    port = "5432",
                    database = "postgres")
        self.cur = self.conn.cursor()

    def searchBookbyId(self, bookID):
        self.cur.execute('SELECT * FROM livro WHERE id = {}'.format(bookID))
        return self.cur.fetchall()[0]

    def searchBookbyName(self, bookName):
        self.cur.execute('SELECT * FROM livro WHERE titulo = {}'.format(bookName))
        return self.cur.fetchall()

    def searchClientbyCpf(self, clientCpf):
        self.cur.execute('SELECT nome FROM cliente WHERE cpf = \'{}\''.format(clientCpf))
        return self.cur.fetchall()[0]

    def searchClientbyName(self, clientName):
        self.cur.execute('SELECT * FROM cliente WHERE nome = {}'.format(clientName))
        return self.cur.fetchall()

    def registerBook(self, title, author, company, edition):
        self.cur.execute('insert into livro (titulo, autor, editora, edicao) values (\'{}\', \'{}\', \'{}\', {});'.format(title, author, company, edition))
        self.conn.commit()

    def registerClient(self, cpf, name, phone, adress):
        self.cur.execute('insert into cliente values (\'{}\', \'{}\', \'{}\', \'{}\');'.format(cpf, name, phone, adress))
        self.conn.commit()

    def removeBook(self, bookID):
        self.cur.execute('delete from livro where id=\'{}\';'.format(bookID))
        self.conn.commit()

    def removeClient(self, cpf):
        self.cur.execute('delete from cliente where cpf=\'{}\';'.format(cpf))
        self.conn.commit()
    
    def rentBook(self, bookID, cpf):
        self.cur.execute('insert into livros_alugados (id_livro, nome_livro, cpf_cliente) SELECT l.id, l.titulo, c.cpf FROM cliente c, livro l WHERE l.id={} and c.cpf=\'{}\';'.format(bookID, cpf))
        rent = datetime.date.today()
        ret = datetime.date(rent.year, rent.month+1, rent.day)
        self.cur.execute('UPDATE livros_alugados SET data_emprestimo=\'{}\', data_devolucao=\'{}\' WHERE id_aluguel=(select max(id_aluguel) from livros_alugados)'.format(rent, ret))
        self.conn.commit()

    def returnBook(self, aluguelID):
        self.cur.execute('delete from livros_alugados where id_aluguel={};'.format(aluguelID))
        self.conn.commit()

    def showRented(self):
        self.cur.execute('SELECT * FROM livros_alugados')
        return self.cur.fetchall()