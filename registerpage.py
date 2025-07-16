from tkinter import *


class registerstudant():
    def __init__(self, root ,voltar):
        self.root = root
        self.options2()
        self.frames()
        self.voltar = voltar
        self.botoes()
        # self.root.mainloop()

    def options2(self):
        self.root.title('Registro de Alunos')
        self.root.geometry('800x600')

    def frames(self):
        self.frame1 = Frame(self.root, background='white')
        self.frame1.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.93)

    def botoes(self):
        self.botaoalterarturma = Button(self.frame1, text='VOLTAR', background='#2857bd', fg='white', relief='groove',
                                         borderwidth=4, command=self.voltar)
        self.botaoalterarturma.place(relx=0.15, rely=0.42, relheight=0.1, relwidth=0.75)
        
    

# registerstudant()