from tkinter import font
import tkinter as Tk

class arialrelative():
    def __init__(self, root):
        self.root = root

    def relativearial(self, event):
        largura = self.root.winfo_width()
        newsize = max(4, int(largura / 70))
        self.relbotaoresp.configure(size=newsize)

    def options(self):
        self.relbotaoresp = font.Font(family='Arial', size=12, weight='bold')
        self.root.bind('<Configure>', self.relativearial)
        return self.relbotaoresp

class optusrelative():
    def __init__(self, root):
        self.root = root

    def relativeaptos(self, event):
        largura = self.root.winfo_width()
        newsize = max(8, int(largura/30))
        self.reloptus.configure(size=newsize)

    def options(self):
        self.reloptus = font.Font(family='Aptos', size=18, weight='bold')
        self.root.bind('<Configure>', self.relativeaptos)
        return self.reloptus



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