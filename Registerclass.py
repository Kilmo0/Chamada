from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from fonts_placeholers import *


class registerclass():
    def __init__(self, root, voltar):
        self.root = root
        self.opções()
        self.frames()
        self.voltar = voltar
        self.labels()
        self.botoes()
        self.entrys()

    def interativefont(self, event):
        largura = self.root.winfo_width()
        newsize = max(8, int(largura / 65))
        self.arialinterative.configure(size=newsize)


    def opções(self):
        self.root.title('Registro de Alunos')
        self.root.geometry('800x600')
        self.arialinterative = font.Font(family='Arial', size=25, weight='bold')
        self.root.bind('<Configure>', self.interativefont)

    def frames(self):
            self.frame1 = Frame(self.root, background='#e7ebfc')
            self.frame1.place(relx=0.02, rely=0.02, relheight=0.95, relwidth=0.95)

    def labels(self):
        self.labelnometurma = Label(self.frame1, text='Nome da turma', background='#e7ebfc', font=self.arialinterative)
        self.labelnometurma.place(relx=0.03, rely=0.18, relheight=0.08, relwidth=0.2)
    
    def entrys(self):
        self.turmaentry = placeholderentry(self.frame1, placeholder='Segunda-Feira 15:00 - 16:30')
        self.turmaentry.place(relx=0.05, rely=0.25, relheight=0.05, relwidth=0.45)


    def botoes(self):
        self.imagevoltaroriginal = Image.open("voltarbotao.png")
        self.imagevoltarredimencionada = self.imagevoltaroriginal.resize((100, 50), Image.LANCZOS)
        self.imagembotao = ImageTk.PhotoImage(self.imagevoltarredimencionada)
        self.botaoalterarturma = Button(self.frame1, image=self.imagembotao, borderwidth=1, relief='flat', background='#e7ebfc', command=self.voltar)
        self.botaoalterarturma.place(relx=0.02, rely=0.02, relheight=0.1, relwidth=0.1)
        self.botaoconfirmar = Button(self.frame1, text='Confirmar',fg='white', borderwidth=4, relief='groove', background='#2857bd', font=self.arialinterative)
        self.botaoconfirmar.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.37)