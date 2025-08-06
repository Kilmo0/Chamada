from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from fonts_placeholers import *


class studantcall():
    def __init__(self, root, voltar):
        self.root = root
        self.opções()
        self.frames()
        self.voltar = voltar
        self.botoes()
        

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

    def botoes(self):
        self.imagevoltaroriginal = Image.open("voltarbotao.png")
        self.imagevoltarredimencionada = self.imagevoltaroriginal.resize((100, 50), Image.LANCZOS)
        self.imagembotao = ImageTk.PhotoImage(self.imagevoltarredimencionada)
        self.botaoalterarturma = Button(self.frame1, image=self.imagembotao, borderwidth=1, relief='flat', background='#e7ebfc', command=self.voltar)
        self.botaoalterarturma.place(relx=0.02, rely=0.02, relheight=0.1, relwidth=0.1)
        self.botaoconfirmar = Button(self.frame1, text='Confirmar',fg='white', borderwidth=4, relief='groove', background='#2857bd', font=self.arialinterative)
        self.botaoconfirmar.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.37)

        
    

# registerstudant()