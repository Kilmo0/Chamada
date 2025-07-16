from tkinter import *
import tkinter as tk
from tkinter import font
import sqlite3
from registerpage import registerstudant
from Registerclass import registerclass

aluno = 'Kaua'
root = tk.Tk()


class relativefonts():
    def relativeaptos(self, event):
        largura = root.winfo_width()
        newsize = max(8, int(largura / 40))
        self.tituloresponsivo.configure(size=newsize)
    def relativearial(self, event):
        largura = root.winfo_width()
        newsize = max(4, int(largura / 70))
        self.relbotaoresp.configure(size=newsize)


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


class APP(mysql, relativefonts):
    def __init__(self):
        self.root = root
        self.options()
        self.frames()
        self.label()
        self.botoes()
        self.root.mainloop()

    def options(self):
        self.root.title('Chamada Alunos')         
        self.root.geometry('800x600')
        self.root.minsize(width=800, height=600)
        self.root.maxsize(1920, 1080)
        self.tituloresponsivo = font.Font(family='Aptos', size=20, weight='bold')
        self.root.bind('<Configure>', self.relativeaptos)
        self.relbotaoresp = font.Font(family='Arial', size=10, weight='bold')
        self.root.bind('<Configure>', self.relativearial)
        

    def frames(self):
        self.framebackground = Frame(self.root, background="#dedede")
        self.framebackground.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frame1 = Frame(self.root, background="#e7ebfc")
        self.frame1.place(relx=0.02, rely=0.02, relheight=0.95, relwidth=0.5)
        self.frame2 = Frame(self.root, background='#e7ebfc')
        self.frame2.place(relx=0.5, rely=0.02, relheight=0.95, relwidth=0.48)
        self.centerline = Frame(self.root, background='Black')
        self.centerline.place(relx=0.49, rely=0.02, relheight=0.95, relwidth=0.03)

    def label(self):
        self.labelregister = Label(self.frame1, text='Registrar Aluno', fg='#1A2C56', bg='#e7ebfc', font=self.tituloresponsivo)
        self.labelregister.place(relx=0.1, rely=0.02, relwidth=0.7, relheight=0.2)
        self.labelchamada = Label(self.frame2, text='Chamada', fg='#1A2C56', bg='#e7ebfc', font=self.tituloresponsivo)
        self.labelchamada.place(relx=0.2, rely=0.02, relwidth=0.7, relheight=0.2)

    def botoes(self):
        self.botaoregistraraluno = Button(self.frame1, text='Registrar Aluno', background="#2857bd", fg='white', relief='groove',
                                           borderwidth=4,font=self.relbotaoresp, command=self.registerstudant )
        self.botaoregistraraluno.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.75)
        self.botaocriarturma = Button(self.frame1, text='Criar Turma', background='#2857bd', fg='white', relief='groove', 
                                      borderwidth=4, font=self.relbotaoresp, command=self.registerclassfun)
        self.botaocriarturma.place(relx=0.1, rely=0.42, relwidth=0.75, relheight=0.1)
        self.botaochamada = Button(self.frame2, text='Chamada', background='#2857bd', fg='white', relief='groove', 
                                   borderwidth=4, font=self.relbotaoresp)
        self.botaochamada.place(relx=0.15, rely=0.3, relheight=0.1, relwidth=0.75)
        self.botaoalterarturma = Button(self.frame2, text='Alterar Turma', background='#2857bd', fg='white', relief='groove',
                                         borderwidth=4, font=self.relbotaoresp)
        self.botaoalterarturma.place(relx=0.15, rely=0.42, relheight=0.1, relwidth=0.75)

    def ocultarframes(self):
        self.frame1.place_forget()
        self.frame2.place_forget()
        self.centerline.place_forget()

    def registerstudant(self):
        self.ocultarframes()
        self.registerpage = registerstudant(self.root, self.voltarmenu)

    def registerclassfun(self):
        self.ocultarframes()
        self.registerclass = registerclass(self.root, self.voltarmenu)

    def voltarmenu(self):
        self.ocultarframes()
        self.__init__()
        

APP()