from tkinter import *
from datetime import date
from datetime import datetime

raiz = Tk()
raiz.geometry("1000x600")
raiz.title("Funciones de fechas")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO ", bg="pink")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))

nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
año = IntVar()

def binario ():
    A=int(dia.get())
    B=int(mes.get())
    C=int(año.get())
    bindia=format(A, '0b' )
    binmes=format(B, '0b')
    binaño=format(C, '0b')

    lblResp['text'] = "La fecha es: {}/{}/{} y  en binario es:{}/{}/{}".format(A,B,C,bindia,binmes,binaño)

def contardia():
    fechaString = f"{año.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strpdate(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    d1 = today
    d2 = date_object
    result1 = abs(d1-d2).days 

    respuesta = f"Usted nacio el {date_object} y ha vivido {result1} días."

    lblResp.configure(text = respuesta)

def contarLetras():
    
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"

    conteoN = len(sNombre)
    conteoA = len(sApellido)
  

    if conteoN % 2 == 0:
        r1 = f"{sNombre} su Nombre es de número Par"
    else:
        r1 = f"{sNombre} su Nombre es de número Inpar"

    if conteoA % 2 == 0:
        r2 = f"{sApellido} su Apellido es de número Par."
    else:
        r2 = f"{sApellido} su Apellido es de número Inpar."

    respuesta = f"{r1} y  {r2} "

    lblResp.configure(text =respuesta )

def vocalConte():
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"
    cuenta = 0
    for carac in sNombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
    for carac in sApellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
    cajita=len(sNombre)
    cajita1=len(sApellido)
    consonante=cajita+cajita1-cuenta

    lblResp['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)

def REVES():
    cajita = nombre.get()+" "+apellido.get()
    cajita = cajita[::-1]
    lblResp["text"] = nombre.get() + " " + apellido.get() + " al revés es: " + cajita

lblnombre= Label(miFrame, text="Nombre:", font = "Helvetica 15")
lblnombre.grid(row=1, column=0)
lblnombre.config(padx=10, pady=20)
txtNombre=Entry(miFrame, textvariable =nombre, font = "Helvetica 15" )
txtNombre.grid(row=1, column=1)


lblapellido=Label(miFrame, text="Apellido:", font = "Helvetica 15")
lblapellido.grid(row=2, column=0)
lblapellido.config(padx=10, pady=10)
txtApellido=Entry(miFrame, textvariable =apellido, font = "Helvetica 15")
txtApellido.grid(row=2, column=1)

lbldia=Label(miFrame, text="Día:", font = "Helvetica 15")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia, font = "Helvetica 15")
txtDia.grid(row=3, column=1)

lblmes=Label(miFrame, text="Mes:", font = "Helvetica 15")
lblmes.grid(row=4, column=0)
lblmes.config(padx=10, pady=10)
txtMes=Entry(miFrame, textvariable =mes, font = "Helvetica 15")
txtMes.grid(row=4, column=1)

lblano=Label(miFrame, text="Año:", font = "Helvetica 15")
lblano.grid(row=5, column=0)
lblano.config(padx=10, pady=10)
txtano=Entry(miFrame, textvariable =año, font = "Helvetica 15")
txtano.grid(row=5, column=1)

btnFuncion1 = Button(miFrame, text="Función 1",command=binario, bg="pink", font=("verdana",12))
btnFuncion1.grid(row=6, column=0)
btnFuncion1.config(padx=10, pady=10)
btnFuncion2 = Button(miFrame, text = "Función 2", command=contardia, bg="pink", font=("verdana",12))
btnFuncion2.grid(row=6, column=1)
btnFuncion2.config(padx=12, pady=10)
btnFuncion3 = Button(miFrame, text = "Función 3", command=contarLetras, bg="pink", font=("verdana",12))
btnFuncion3.grid(row=6, column=2)
btnFuncion3.config(padx=14, pady=10)
btnFuncion4 = Button(miFrame, text = "Función 4", command=vocalConte, bg="pink", font=("verdana",12))
btnFuncion4.grid(row=6, column=3)
btnFuncion4.config(padx=16, pady=10)
btnFuncion5 = Button(miFrame, text = "Función 5", command=REVES, bg="pink", font=("verdana",12))
btnFuncion5.grid(row=6, column=4)
btnFuncion5.config(padx=18, pady=10)

lblResp=Label(miFrame, text="Respuesta:", font = "Helvetica 10")
lblResp.grid(row=9, column=1)
lblResp.config(padx=10, pady=10)
lblR=Label(miFrame, font = "Helvetica 15")
lblR.grid(row=10, column=0)
lblR.config(padx=10, pady=10)

raiz.mainloop()