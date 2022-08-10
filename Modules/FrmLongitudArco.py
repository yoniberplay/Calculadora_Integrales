from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox as MessageBox
from sympy import diff,integrate,sqrt,symbols,init_printing,plotting
from datetime import datetime

class frm_longitud_arco(Frame):
    def __init__(self, root=  None):
        super().__init__(root,width=650,height=500,background="#F3F4ED")
        self.x = symbols("x")
        init_printing(use_unicode=True)
        root.title("Calculador de longitud de arco (Aplicación de Integral)") 
        self.pack()
        self.crear_widget()
    
    #Funcion para insertar caracteres.    
    def setFuction(self,caracter):
        if(self.funcion_entry.focus_get()==self.funcion_entry):
            self.funcion_entry.insert(END,caracter)
        elif(self.limite_inferior_entry.focus_get()==self.limite_inferior_entry):
            self.limite_inferior_entry.insert(END,caracter)
        elif(self.limite_superior_entry.focus_get()==self.limite_superior_entry):
            self.limite_superior_entry.insert(END,caracter)
        
    def limpiar_todo(self):
        self.funcion_entry.delete(0,END)
        self.limite_inferior_entry.delete(0,END)
        self.limite_superior_entry.delete(0,END)
        self.resultado_entry.delete(0,END)
        
    def backspace(self):
        contador=self.funcion_entry.get()
        contador=len(contador)
        contador-=1
        self.funcion_entry.delete(contador,END)

   
    def graficar(self,funcionFX,infLim,supLim): #(3/2)*x**(2/3)+4
       try:
           if(self.validar_campos()):
            List = []
            #Primero derivamos las funcion.
            diferenciaFX = diff(funcionFX, self.x)
            #Segundo ejecutamos la Funcion de la longitud de arco:
            funIntegral = sqrt(1 + (diferenciaFX)**2)
            #Aplicando la formula de longitud de arco evaluando la :
            longArcoExpre = integrate(funIntegral,self.x)

            inf = longArcoExpre.subs(self.x,infLim)
            sup = longArcoExpre.subs(self.x,supLim)
                        
            longArcoNeta = sup-inf
            List.append(funcionFX)
            List.append(diferenciaFX)
            List.append(funIntegral)
            List.append((infLim,supLim))
            List.append(longArcoExpre)
            List.append(longArcoNeta.evalf())

            self.resultado_entry.insert(END, List[-1])

       except:
            MessageBox.showinfo(title="Error",message="Debe introducir la funcion correctamente.!")


    def graficar_funcion(self):
        if(self.validar_campos()):
            funcionFX = self.funcion_entry.get()
            graph = plotting.plot(funcionFX,(self.x,self.limite_inferior_entry.get(),self.limite_superior_entry.get()),show=False,title="f(x)")
            datetime_now = str(datetime.now().timestamp())
            graph.save(f"./Resources/Graphs/{datetime_now}.png")
            back = graph.backend(graph)
            back.process_series()

            back.show()
               
    def validar_campos(self):
        isValid = True
        if(self.limite_inferior_entry.get() == "" or self.limite_superior_entry.get() == ""):
            result = MessageBox.askquestion(title="Debe introducir los limites.", message="Debe introducir los limites. \n Si no especifica, los limites por defecto estos serán [-1 , 1]. ¿Está de acuerdo con esta selección?")
            if(result == MessageBox.YES):
                self.limite_inferior_entry.insert(END,"1")
                self.limite_superior_entry.insert(END,"-1")
                isValid = True
            else:
                isValid = False
                MessageBox.showinfo(title="Error", message="Faltan los límites de integración")
            
            if(self.funcion_entry.get() == ""):
                MessageBox.showerror(title="Error", message="Falta la función")
                isValid = False
        return isValid


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

        # Boton de resultado.

        self.grafica_btn = Button(self, text="Grafica", width=7, height=2, relief="solid", background="#377DFF",
                                  command=lambda: self.graficar_funcion())
        self.grafica_btn.grid(row=10, column=3)

        self.integral_btn = Button(self, text="=", width=7, height=2, relief="solid", background="#0a729d",
                                   command=lambda :self.graficar(self.funcion_entry.get(),self.limite_superior_entry.get(),self.limite_inferior_entry.get()))
        self.integral_btn.grid(row=10, column=4)