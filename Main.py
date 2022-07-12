import tkinter
from webbrowser import *
from tkinter import *
from tkinter.font import BOLD
from Modules.FrmIntIndefinidas import frm_integral_indefinida
from Modules.FrmIntDefinidas import frm_integral_definida
from Modules.FrmLongitudArco import frm_longitud_arco

from PIL import ImageTk, Image

class Main(Frame):
    def __init__(self, root=  None):
        super().__init__(root, width=650, height=500, background="#EBEFFA")
        self.root=root
        self.pack()
        self.crear_Widget()

    # funcion para abrir indefinidas
    def open_indefinida(self):
        root=Tk()
        frm_integral_indefinida(root)
        root.eval("tk::PlaceWindow . center")
        root.title("Integrales Indefinidas")
        root.iconbitmap("./Resources/portadalibro.ico")
        root.resizable(False, False)
        root.mainloop()

    # funcion para abrir definidas
    def open_definida(self):
        root=Tk()
        frm_integral_definida(root)
        root.eval("tk::PlaceWindow . center")
        root.title("Integrales Definidas")
        root.iconbitmap("./Resources/portadalibro.ico")
        root.resizable(False, False)
        root.mainloop()

    # funcion para abrir indefinidas
    def open_longitud_arco(self):
        root=Tk()
        frm_longitud_arco(root)
        root.eval("tk::PlaceWindow . center")
        root.title("Longitud del arco ")
        root.iconbitmap("./Resources/portadalibro.ico")
        root.resizable(False, False)
        root.mainloop()

    # funcion para abrir la documentacion
    def open_verdocumentacion(self):
        open_new("https://github.com/christopherjael")

    # funcion para abrir developer by
    def open_verdeveloperby(self):
        open_new("https://github.com/yoniberplay")



    def crear_Widget(self):
        Label(self,text="Seleccione el tipo de integral a resolver",font=("arial",14,BOLD),background="#EBEFFA").place(x=150,y=20)

        # boton para abrir la calculadora de indefinidas
        self.B7=tkinter.Button(self,text="Indefinida",padx=30,pady=10,bg="#33B4F1",fg="#EBEFFA",width=20,
        font=("verdana",8,BOLD),command=self.open_indefinida)
        self.B7.place(x=215,y=420)

        # boton para abrir la calculadora de definidas
        self.B7=tkinter.Button(self,text="Definida",bg="#33B4F1",fg="#EBEFFA",width=20,
        font=("verdana",8,BOLD),padx=30,pady=10,command=self.open_definida)
        self.B7.place(x=215,y=370)

        # boton para abrir la calculadora de longitud de arco
        self.B7=tkinter.Button(self,text="Longitud de arco",width=20,
        font=("verdana",8,BOLD),padx=30,pady=10,bg="#33B4F1",fg="#EBEFFA",command=self.open_longitud_arco)
        self.B7.place(x=215,y=320)

        # boton para abrir el manual de usuarios
        self.B7 = tkinter.Button(self, text="Manual de usuario",
        font=("times", 10, "underline"), bg="#EBEFFA",bd=0,cursor="hand2",command=self.open_verdocumentacion)
        self.B7.place(x=10, y=470)

        # boton para abrir developer by
        self.B7 = tkinter.Button(self, text="Developed by",font=("times", 10, "underline"), bg="#EBEFFA", bd=0, cursor="hand2",command=self.open_verdeveloperby)
        self.B7.place(x=550, y=470)

root=Tk()
app=Main(root)
root.iconbitmap("./Resources/portadalibro.ico")
root.title("Calculadora de integrales")
ima1=ImageTk.PhotoImage(Image.open("./Resources/portadalibro.ico"))
Label(root,image=ima1,bg="#EBEFFA").place(x=225,y=55)

root.eval("tk::PlaceWindow . center")
root.resizable(False,False)
app.mainloop()

