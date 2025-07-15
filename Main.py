from tkinter import *
import sqlite3

aluno = 'Kaua'
root = Tk()

class mysql():
    def sqlconnect(self):
        self.conn = sqlite3.connect(f'{aluno}.db')
        self.cursor = self.conn.cursor()
    def sqldisconnect(self):
        self.conn.close()
    def studantsactives(self):
        self.sqlconnect()
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
            cod INTEGER PRIMARY KEY,
            studant CHAR(40) NOT NULL,
            phone INTEGER 
        );""")
        self.conn.commit(); print('Banco de Dados criado com sucesso')
        self.sqldisconnect()


    # def registersystem():


class APP(mysql):
    def __init__(self):
        self.root = root
        self.options()
        self.frames()
        self.label()
        self.root.mainloop()

    def options(self):
        self.root.title('Chamada Alunos')         
        self.root.geometry('800x600')
        self.root.minsize(width=800, height=600)
        self.root.maxsize(1920, 1080)

    def frames(self):
        self.framebackground = Frame(self.root, background="#dedede")
        self.framebackground.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frame1 = Frame(self.root, background='white')
        self.frame1.place(relx=0.02, rely=0.02, relheight=0.95, relwidth=0.5)
        self.frame2 = Frame(self.root, background='White')
        self.frame2.place(relx=0.5, rely=0.02, relheight=0.95, relwidth=0.48)
        self.centerline = Frame(self.root, background='Black')
        self.centerline.place(relx=0.49, rely=0.02, relheight=0.95, relwidth=0.03)

    def label(self):
        self.labelregister = Label(self.frame1, text='Registrar Aluno', fg='#1A2C56', font=('Aptos', 20))
        self.labelregister.place(relx=0.4, rely=0.07, relwidth=0.9, relheight=0.9)

APP()