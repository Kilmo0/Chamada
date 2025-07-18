from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import font
import tkinter as Tk

class placeholderentry(Tk.Entry):
    def __init__(self, master=None, placeholder='Exemplo', corplaceholder='gray', *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.corplaceholder = corplaceholder
        self.cornormal = self['fg']

        self.bind('<FocusIn>', self.aofocar)
        self.bind('<FocusOut>', self.aosair)

        self.putplaceholder()
    
    def putplaceholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.corplaceholder

    def aofocar(self, _):
        if self.get() == self.placeholder:
            self.delete(0, Tk.END)
            self['fg'] = self.corplaceholder

    def aosair(self, _):
        if not self.get():
            self.putplaceholder()



class registerstudant():
    def __init__(self, root ,voltar):
        self.root = root
        self.options2()
        self.frames()
        self.voltar = voltar
        self.labels()
        self.botoes()
        self.entrys()

    def interativefont(self, event):
        largura = self.root.winfo_width()
        newsize = max(8, int(largura / 65))
        self.arialinterative.configure(size=newsize)


    def options2(self):
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
    
    def labels(self):
        self.labelnome = Label(self.frame1, text='Nome', background='#e7ebfc', fg='black', font=self.arialinterative)
        self.labelnome.place(relx=0.035, rely=0.2, relheight=0.05, relwidth=0.1)
        self.labeltelefone = Label(self.frame1, text='Telefones', background='#e7ebfc', fg='black', font=self.arialinterative)
        self.labeltelefone.place(relx=0.05, rely=0.33, relheight=0.05, relwidth=0.1)
        

    def entrys(self):
        self.entrynome = placeholderentry(self.frame1, placeholder='Kauã Lorenzi', font=('Arial', 10, 'bold'))
        self.entrynome.place(relx=0.05, rely=0.25, relheight=0.05, relwidth=0.5)
        self.entrytele = placeholderentry(self.frame1, placeholder='47999223296', font=('Arial', 10, 'bold'))
        self.entrytele.place(relx=0.05, rely=0.38, relheight=0.05, relwidth=0.5)
        self.entrytele2 = placeholderentry(self.frame1, placeholder='47999223296', font=('Arial', 10, 'bold'))
        self.entrytele2.place(relx=0.05, rely=0.45, relheight=0.05, relwidth=0.5)
        
        
    
