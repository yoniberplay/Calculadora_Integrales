from os import close
from tkinter import *
import tkinter
from tkinter.font import BOLD, ITALIC, families
from matplotlib.pyplot import winter
from sympy.utilities.iterables import rotations
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
    def createWidget(self):
        Label(self,text="Seleccione el tipo de integral a resolver",font=("arial",14,BOLD),background="#EBEFFA").place(x=150,y=20)
        ##Label(self,text="Seleccione su integral:",font=("verdana",12,BOLD,ITALIC),background="#f2968a").place(x=250,y=310)
        
        self.B7=tkinter.Button(self,text="Indefinida",padx=30,pady=10,bg="#33B4F1",width=20,
        font=("verdana",8,BOLD,ITALIC),command=self.Close1)
        self.B7.place(x=215,y=420)
        
        self.B7=tkinter.Button(self,text="Definida",bg="#33B4F1",width=20,
        font=("verdana",8,BOLD,ITALIC),padx=30,pady=10,command=self.Close2)
        self.B7.place(x=215,y=370)
        
        self.B7=tkinter.Button(self,text="Longitud de arco",width=20,
        font=("verdana",8,BOLD,ITALIC),padx=30,pady=10,bg="#33B4F1",command=self.Close3)
        self.B7.place(x=215,y=320)
        

root=Tk()
app=Principal(root)
root.iconbitmap("./Img/portadalibro.ico")
root.title("Calculadora de integrales")
ima1=ImageTk.PhotoImage(Image.open("./Img/portadalibro.ico"))
Label(root,image=ima1,bg="#EBEFFA").place(x=225,y=55)
Label(root,text="Yoniber Encarnacion 2021-1442 || Brian Peña 2021-0948 || Christopher Montero 2021-0622 || Charles Alexandre Meance 2021-9503",bg="#EBEFFA",font=("arial",8,BOLD)).place(x=10,y=470)

##ima2=ImageTk.PhotoImage(Image.open("./Img/diseño1.ico"))
##Label(root,image=ima2,bg="#f2968a").place(x=400,y=100)

root.eval( 'tk::PlaceWindow . center') #Esto es un codigo ..jjaaj...para centrar la ventana..
root.resizable(0,0)
app.mainloop()

