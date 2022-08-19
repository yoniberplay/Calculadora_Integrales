from tkinter import *
from tkinter.font import *
from sympy import*

class frm_integral_definida(Frame):
    def __init__(self, root=None):
        super().__init__(root,width=650,height=500,background="white")
        self.root=root
        self.pack()
        self.crear_widget()


    def setFuction(self,fuction):
        if(self.funcion_entry.focus_get()==self.funcion_entry):
            self.funcion_entry.insert(END, fuction)
        elif(self.limite_inferior_entry.focus_get() == self.limite_inferior_entry):
            self.limite_inferior_entry.insert(END, fuction)
        elif(self.limite_superior_entry.focus_get() == self.limite_superior_entry):
            self.limite_superior_entry.insert(END, fuction)

    def limpiar_todo(self):
        self.resultado_entry.config(state="normal")
        self.funcion_entry.delete(0, END)
        self.resultado_entry.delete(0, END)
        self.limite_inferior_entry.delete(0, END)
        self.limite_superior_entry.delete(0, END)
        self.funcion_entry.focus()

    def backspace(self):

        if(self.funcion_entry.focus_get()==self.funcion_entry):
            contador=self.funcion_entry.get()
            contador=len(contador) - 1
            self.funcion_entry.delete(contador, END)
        elif(self.limite_inferior_entry.focus_get() == self.limite_inferior_entry):
            contador=self.limite_inferior_entry.get()
            contador=len(contador)
            contador-=1
            self.limite_inferior_entry.delete(contador, END)
            
        elif(self.limite_superior_entry.focus_get() == self.limite_superior_entry):
            contador=self.limite_superior_entry.get()
            contador=len(contador)
            contador-=1
            self.limite_superior_entry.delete(contador, END)
        elif(self.resultado_entry.focus_get() == self.resultado_entry):
            contador=self.resultado_entry.get()
            contador=len(contador)
            contador-=1
            self.resultado_entry.delete(contador, END)
            

    def resultado(self): #@Yoniber Encarnacion
        try:
            sym = None
            funcion_string = self.funcion_entry.get()
            if("x" in funcion_string):
                sym = Symbol("x")
            elif("y" in funcion_string):
                sym = Symbol("y")

            if(self.funcion_entry.get()!= "" and self.limite_inferior_entry.get()!= "" and self.limite_superior_entry.get()!= ""):
                self.resultado_entry.delete(0, END)
                self.resultado_entry.insert(END, integrate(self.funcion_entry.get(), (sym, self.limite_inferior_entry.get(), self.limite_superior_entry.get())))
            else:
                self.resultado_entry.delete(0, END)
                self.resultado_entry.insert(END, "Error.. Debe rellenar todos los campos.")
        except SympifyError:
            self.resultado_entry.insert(END, "Error.")
            
    ##--------------> creación de los widget<---------------------------------
    def crear_widget(self):

        # Funcion y resultado
        self.funcion_label = Label(self, text="Función", background="white", font=("verdana", 8, BOLD))
        self.funcion_label.grid(row=0, column=0)

        self.funcion_entry = Entry(self, relief="solid", justify='center', font="Arial 13", width=20)
        self.funcion_entry.grid(row=1, column=0, columnspan=3, ipady=10)
        self.funcion_entry.focus()

        self.resultado_label = Label(self, text="Resultado", background="white", font=("verdana", 8, BOLD))
        self.resultado_label.grid(row=2, column=0)

        self.resultado_entry = Entry(self, relief="solid", justify='center', font="Arial 13", width=20)
        self.resultado_entry.grid(row=3, column=0, columnspan=3, ipady=10, pady=10)

        # Limite superior y inferior
        self.limite_superior_label = Label(self, text="Limite superior", background="white", font=("verdana", 8, BOLD))
        self.limite_superior_label.grid(row=0, column=3)

        self.limite_superior_entry = Entry(self, relief="solid", justify='center', font="Arial 13", width=15)
        self.limite_superior_entry.grid(row=1, column=3, columnspan=5, ipady=10, pady=10)

        self.limite_inferior_label = Label(self, text="Limite inferior", background="white", font=("verdana", 8, BOLD))
        self.limite_inferior_label.grid(row=2, column=3)

        self.limite_inferior_entry = Entry(self, relief="solid", justify='center', font="Arial 13", width=15)
        self.limite_inferior_entry.grid(row=3, column=3, columnspan=5, ipady=10, pady=10)

        # Funciones Trigonometricas
        self.sin_btn = Button(self, text="sin", relief="solid", width=7, height=2, background="#377DFF",
                              command=lambda: self.setFuction("sin("))
        self.sin_btn.grid(row=5, column=0)

        self.cos_btn = Button(self, text="cos", relief="solid", width=7, height=2, background="#377DFF",
                              command=lambda: self.setFuction("cos("))
        self.cos_btn.grid(row=5, column=1)

        self.tan_btn = Button(self, text="tan", relief="solid", width=7, height=2, background="#377DFF",
                              command=lambda: self.setFuction("tan("))
        self.tan_btn.grid(row=5, column=2, padx=5)

        self.sec_btn = Button(self, text="sec", relief="solid", width=7, height=2, background="#377DFF",
                              command=lambda: self.setFuction("sec("))
        self.sec_btn.grid(row=6, column=0, pady=5)

        self.csc_btn = Button(self, text="csc", relief="solid", width=7, height=2, background="#377DFF",
                              command=lambda: self.setFuction("csc("))
        self.csc_btn.grid(row=6, column=1)

        self.cot_btn = Button(self, text="cot", relief="solid", width=7, height=2, background="#377DFF",
                              command=lambda: self.setFuction("cot("))
        self.cot_btn.grid(row=6, column=2)

        # Teclado Numerico
        self.uno_btn = Button(self, text="1", relief="solid", width=7, height=2, background="white",
                              command=lambda: self.setFuction("1"))
        self.uno_btn.grid(row=7, column=0, pady=5)

        self.dos_btn = Button(self, text="2", relief="solid", width=7, height=2, background="white",
                              command=lambda: self.setFuction("2"))
        self.dos_btn.grid(row=7, column=1)

        self.tres_btn = Button(self, text="3", relief="solid", width=7, height=2, background="white",
                               command=lambda: self.setFuction("3"))
        self.tres_btn.grid(row=7, column=2)

        self.cuatro_btn = Button(self, text="4", relief="solid", width=7, height=2, background="white",
                                 command=lambda: self.setFuction("4"))
        self.cuatro_btn.grid(row=8, column=0, pady=5)

        self.cinco_btn = Button(self, text="5", relief="solid", width=7, height=2, background="white",
                                command=lambda: self.setFuction("5"))
        self.cinco_btn.grid(row=8, column=1)

        self.seis_btn = Button(self, text="6", relief="solid", width=7, height=2, background="white",
                               command=lambda: self.setFuction("6"))
        self.seis_btn.grid(row=8, column=2)

        self.siete_btn = Button(self, text="7", relief="solid", width=7, height=2, background="white",
                                command=lambda: self.setFuction("7"))
        self.siete_btn.grid(row=9, column=0, pady=5)

        self.ocho_btn = Button(self, text="8", relief="solid", width=7, height=2, background="white",
                               command=lambda: self.setFuction("8"))
        self.ocho_btn.grid(row=9, column=1)

        self.nueve_btn = Button(self, text="9", relief="solid", width=7, height=2, background="white",
                                command=lambda: self.setFuction("9"))
        self.nueve_btn.grid(row=9, column=2)

        self.punto_btn = Button(self, text=".", relief="solid", width=7, height=2, background="white",
                                command=lambda: self.setFuction("."))
        self.punto_btn.grid(row=10, column=0, pady=5)

        self.cero_btn = Button(self, text="0", relief="solid", width=7, height=2, background="white",
                               command=lambda: self.setFuction("0"))
        self.cero_btn.grid(row=10, column=1)

        self.pi_btn = Button(self, text="π", width=7, height=2, relief="solid", background="#377DFF",
                             command=lambda: self.setFuction("pi"))
        self.pi_btn.grid(row=10, column=2)

        # Operaciones expeciales
        self.abrir_parentesis_btn = Button(self, text="(", width=7, height=2, relief="solid", background="#377DFF",
                                           command=lambda: self.setFuction("("))
        self.abrir_parentesis_btn.grid(row=5, column=3)

        self.cerrar_parentesis_btn = Button(self, text=")", width=7, height=2, relief="solid", background="#377DFF",
                                            command=lambda: self.setFuction(")"))
        self.cerrar_parentesis_btn.grid(row=5, column=4)

        self.potencia_btn = Button(self, text="x^", width=7, height=2, relief="solid", background="#377DFF",
                                   command=lambda: self.setFuction("**"))
        self.potencia_btn.grid(row=6, column=3)

        self.raiz_btn = Button(self, text="√", width=7, height=2, relief="solid", background="#377DFF",
                               command=lambda: self.setFuction("sqrt("))
        self.raiz_btn.grid(row=6, column=4)

        self.log_btn = Button(self, text="Log", width=7, height=2, relief="solid", background="#377DFF",
                              command=lambda: self.setFuction("log("))
        self.log_btn.grid(row=4, column=0, pady=5)

        self.variable_x_btn = Button(self, text="x", width=7, height=2, relief="solid", background="#377DFF",
                                     command=lambda: self.setFuction("x"))
        self.variable_x_btn.grid(row=4, column=1)

        self.variable_y_btn = Button(self, text="y", width=7, height=2, relief="solid", background="#377DFF",
                                     command=lambda: self.setFuction("y"))
        self.variable_y_btn.grid(row=4, column=2)

        # Botones de limpieza

        self.ac_btn = Button(self, text="AC", relief="solid", width=7, height=2, background="#f0463a",
                             command=self.limpiar_todo)
        self.ac_btn.grid(row=7, column=3, padx=10)

        self.del_btn = Button(self, text="DEL", relief="solid", width=7, height=2, background="#f0463a",
                              command=self.backspace)
        self.del_btn.grid(row=7, column=4)

        # Operaciones aritmeticas
        self.mas_btn = Button(self, text="+", width=7, height=2, relief="solid", background="gray",
                              command=lambda: self.setFuction("+"))
        self.mas_btn.grid(row=8, column=3)

        self.menos_btn = Button(self, text="-", width=7, height=2, relief="solid", background="gray",
                                command=lambda: self.setFuction("-"))
        self.menos_btn.grid(row=8, column=4)

        self.multiplicar_btn = Button(self, text="*", width=7, height=2, relief="solid", background="gray",
                                      command=lambda: self.setFuction("*"))
        self.multiplicar_btn.grid(row=9, column=3)

        self.division_btn = Button(self, text="÷", width=7, height=2, relief="solid", background="gray",
                                   command=lambda: self.setFuction("/"))
        self.division_btn.grid(row=9, column=4)

        # Boton de resultado y etc

        self.num_natural_btn = Button(self, text="e", width=7, height=2, relief="solid", background="#377DFF",
                                      command=lambda: self.setFuction("e("))
        self.num_natural_btn.grid(row=10, column=3)

        self.integral_btn = Button(self, text="=", width=7, height=2, relief="solid", background="#0a729d",
                                   command=self.resultado)
        self.integral_btn.grid(row=10, column=4)