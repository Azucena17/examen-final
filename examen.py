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
ano = IntVar()

def binario ():
    uno=int(dia.get())
    dos=int(mes.get())
    tres=int(anio.get())
    bindia=format(uno, '0b' )
    binmes=format(dos, '0b')
    binanio=format(tres, '0b')

    lblResp['text'] = "La fecha es: {}/{}/{} y  en binario es:{}/{}/{}".format(uno,dos,tres,bindia,binmes,binanio)

def conteoDias():
    fechaString = f"{ano.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    d1 = today
    d2 = date_object
    result1 = abs(d1-d2).days 

    respuesta = f"Usted nacio el {date_object} y ha vivido {result1} días."

    lblResp.configure(text = respuesta)

def conteoLetras():
    #--concatNombApelli = f"{nombre.get()}{apellido.get()}"
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

    def conteoLetras():
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

lbldia=Label(miFrame, text="Día:")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia)
txtDia.grid(row=3, column=1)

lblano=Label(miFrame, text="Año:")
lblano.grid(row=5, column=0)
lblano.config(padx=10, pady=10)
txtano=Entry(miFrame, textvariable =ano)
txtano.grid(row=5, column=1)

btnFuncion1 = Button(miFrame, text="Función 1",command=binario)
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

lblResp=Label(miFrame, text="Respuesta:")
lblResp.grid(row=9, column=0)
lblResp.config(padx=10, pady=10)
lblR=Label(miFrame)
lblR.grid(row=10, column=0)
lblR.config(padx=10, pady=10)