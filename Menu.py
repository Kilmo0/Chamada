from tkinter import *
import tkinter as tk
from studantregister import registerstudant
from Registerclass import registerclass
from chamadapage import studantcall
from alternarturma import alterarturma
from fonts_placeholers import *

aluno = 'Kaua'
root = tk.Tk()


class APP():
    def __init__(self):
        self.root = root
        self.arialrel = arialrelative(self.root)
        self.optusrel = optusrelative(self.root)
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
        self.relbotaoresp = self.arialrel.options()
        self.reloptus = self.optusrel.options()
        

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
        self.labelregister = Label(self.frame1, text='Registrar Aluno', fg='#1A2C56', bg='#e7ebfc', font=self.reloptus)
        self.labelregister.place(relx=0.1, rely=0.02, relwidth=0.7, relheight=0.2)
        self.labelchamada = Label(self.frame2, text='Chamada', fg='#1A2C56', bg='#e7ebfc', font=self.reloptus)
        self.labelchamada.place(relx=0.2, rely=0.02, relwidth=0.7, relheight=0.2)

    def botoes(self):
        self.botaoregistraraluno = Button(self.frame1, text='Registrar Aluno', background="#2857bd", fg='white', relief='groove',
                                           borderwidth=4,font=self.relbotaoresp, command=self.registerstudant )
        self.botaoregistraraluno.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.75)
        self.botaocriarturma = Button(self.frame1, text='Criar Turma', background='#2857bd', fg='white', relief='groove', 
                                      borderwidth=4, font=self.relbotaoresp, command=self.registerclassfun)
        self.botaocriarturma.place(relx=0.1, rely=0.42, relwidth=0.75, relheight=0.1)
        self.botaochamada = Button(self.frame2, text='Chamada', background='#2857bd', fg='white', relief='groove', 
                                   borderwidth=4, font=self.relbotaoresp, command=self.chamadapage)
        self.botaochamada.place(relx=0.15, rely=0.3, relheight=0.1, relwidth=0.75)
        self.botaoalterarturma = Button(self.frame2, text='Alterar Turma', background='#2857bd', fg='white', relief='groove',
                                         borderwidth=4, font=self.relbotaoresp, command=self.alterarturmafun)
        self.botaoalterarturma.place(relx=0.15, rely=0.42, relheight=0.1, relwidth=0.75)
        self.botaoverificaraluno = Button(self.frame2, text='Verificar aluno', background='#2857bd', fg='white', relief='groove',
                                          borderwidth=4, font=self.relbotaoresp)
        self.botaoverificaraluno.place(relx=0.15, rely=0.54, relheight=0.1, relwidth=0.75)

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
    
    def chamadapage(self):
        self.ocultarframes()
        self.studantcall = studantcall(self.root, self.voltarmenu)
    
    def alterarturmafun(self):
        self.ocultarframes()
        self.alterarturma = alterarturma(self.root, self.voltarmenu)

    def voltarmenu(self):
        self.ocultarframes()
        self.__init__()
        

APP()