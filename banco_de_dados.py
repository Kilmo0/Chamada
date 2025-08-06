import sqlite3

class bandodadosalunos():
    def sqlconnect(self, infoname):
        if infoname != None:
            self.conn = sqlite3.connect(f'{infoname}.db')
            self.cursor = self.conn.cursor()

    def sqldisconnect(self):
        self.conn.close()

    def studantsactives(self):
        self.sqlconnect(infoname=None)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
            cod INTEGER PRIMARY KEY,
            student TEXT NOT NULL,
            phone INTEGER,
            phone2 INTEGER
        );""")
        self.conn.commit(); print('Banco de Dados criado com sucesso')

    def sendinfos(self, infoname, infotele, infotele2):
        self.sqlconnect(infoname)
        self.studantsactives()
        self.cursor.execute("""
            INSERT INTO aluno (student, phone, phone2)
            VALUES (?, ?, ?)
            """, (infoname, infotele, infotele2))
        self.conn.commit()
        self.sqldisconnect(); print('SQL DESCONECTADO')

class bancodedadosturma():
    def sqlconnect(self):
        self.conn = sqlite3.connect('testeturma.db')
        self.cursor = self.conn.cursor()
    
    def sqldeconnect(self):
        self.conn.close()
