from tkinter import *
from datetime import date
from datetime import datetime

raiz = Tk()
raiz.geometry("500x500")
raiz.title("Ejecución de Funciones")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))

nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
anio = IntVar()

lblnombre= Label(miFrame, text="Nombre:")
lblnombre.grid(row=1, column=0)
lblnombre.config(padx=10, pady=10)
txtNombre=Entry(miFrame, textvariable =nombre)
txtNombre.grid(row=1, column=1)

lblapellido=Label(miFrame, text="Apellido:")
lblapellido.grid(row=2, column=0)
lblapellido.config(padx=10, pady=10)
txtApellido=Entry(miFrame, textvariable =apellido)
txtApellido.grid(row=2, column=1)

lbldia=Label(miFrame, text="Día: ")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia)
txtDia.grid(row=3, column=1)



btnFuncion1 = Button(miFrame, text="Función 1")
btnFuncion1.grid(row=6, column=0)
btnFuncion1.config(padx=10, pady=10)
btnFuncion2 = Button(miFrame, text = "Función 2", command=conteoDias)
btnFuncion2.grid(row=6, column=1)
btnFuncion2.config(padx=10, pady=10)
btnFuncion3 = Button(miFrame, text = "Función 3", command=conteoLetras)
btnFuncion3.grid(row=7, column=0)
btnFuncion3.config(padx=10, pady=10)
btnFuncion4 = Button(miFrame, text = "Función 4")
btnFuncion4.grid(row=7, column=1)
btnFuncion4.config(padx=10, pady=10)
btnFuncion5 = Button(miFrame, text = "Función 5")
btnFuncion5.grid(row=8, column=0)
btnFuncion5.config(padx=10, pady=10)