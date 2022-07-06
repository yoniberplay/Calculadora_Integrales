import webbrowser
from os import close
from tkinter import *
import tkinter
import webbrowser
from tkinter.font import BOLD, ITALIC, families
from ClassLibrary.indefinida import AppIndefinida
from ClassLibrary.definida import AppDefinida
from ClassLibrary.longitudArco import LongArco

from PIL import ImageTk, Image

class Principal(Frame):
    def __init__(self, root=  None):
        super().__init__(root, width=650, height=500, background="#EBEFFA")
       ## super().__init__(root,width=650,height=500,background="#e6ffd1")
        self.root=root
        self.pack()
        self.createWidget()
    def Close1(self):
        root=Tk()
        AppIndefinida(root)
        root.eval( 'tk::PlaceWindow . center')
        root.mainloop()
        
    def Close2(self):
        root=Tk()
        AppDefinida(root)
        root.eval( 'tk::PlaceWindow . center')
        root.title("Integrales definidas")
        root.iconbitmap("./Img/portadalibro.ico")
        root.resizable(0,0)
        root.mainloop()
        
    def Close3(self):
        root=Tk()
        LongArco(root)
        root.eval( 'tk::PlaceWindow . center')
        root.title("Longitud del arco ")
        root.iconbitmap("./Img/portadalibro.ico")
        root.resizable(0,0)
        root.mainloop()

    def verdocumentacion(self):
        webbrowser.open_new("https://github.com/christopherjael")

    def verdesarrolladores(self):
        webbrowser.open_new("https://github.com/yoniberplay")

    def createWidget(self):
        Label(self,text="Seleccione el tipo de integral a resolver",font=("arial",14,BOLD),background="#EBEFFA").place(x=150,y=20)
        ##Label(self,text="Seleccione su integral:",font=("verdana",12,BOLD,ITALIC),background="#f2968a").place(x=250,y=310)
        
        self.B7=tkinter.Button(self,text="Indefinida",padx=30,pady=10,bg="#33B4F1",fg="#EBEFFA",width=20,
        font=("verdana",8,BOLD),command=self.Close1)
        self.B7.place(x=215,y=420)
        
        self.B7=tkinter.Button(self,text="Definida",bg="#33B4F1",fg="#EBEFFA",width=20,
        font=("verdana",8,BOLD),padx=30,pady=10,command=self.Close2)
        self.B7.place(x=215,y=370)
        
        self.B7=tkinter.Button(self,text="Longitud de arco",width=20,
        font=("verdana",8,BOLD),padx=30,pady=10,bg="#33B4F1",fg="#EBEFFA",command=self.Close3)
        self.B7.place(x=215,y=320)

        self.B7 = tkinter.Button(self, text="Manual de usuario",
        font=("times", 10, "underline"), bg="#EBEFFA",bd=0,cursor="hand2",command=self.verdocumentacion)
        self.B7.place(x=10, y=470)

        self.B7 = tkinter.Button(self, text="Developed by",font=("times", 10, "underline"), bg="#EBEFFA", bd=0, cursor="hand2",command=self.verdesarrolladores)
        self.B7.place(x=550, y=470)

root=Tk()
app=Principal(root)
root.iconbitmap("./Img/portadalibro.ico")
root.title("Calculadora de integrales")
ima1=ImageTk.PhotoImage(Image.open("./Img/portadalibro.ico"))
Label(root,image=ima1,bg="#EBEFFA").place(x=225,y=55)

root.eval( 'tk::PlaceWindow . center')
root.resizable(0,0)
app.mainloop()

