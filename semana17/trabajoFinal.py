import requests as req
import os
from tkinter import messagebox
from tkinter import *



SERVIDOR = "http://pad19.com:3030"
ENDPOINT_PRODUCTOS = "productos/10"
ENDPOINT_PEDIDOS = "pedidos/10"
ENDPOINT_CONSULTA_PEDIDOS = "pedidos/"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgiLCJub21icmUiOiJKdWFuIE1haWRhbmEifQ.Iv6XfvzwAGlo1mw-LoWC3l5bKeW4itVfhy8GMxPTwCE"
URL_TELEGRAM = ""
TOKEN_TELEGRAM = ""
ENDPOINT_TELEGRAM = "sendMessage"
ID_CHAT = ""

def consulta():
    URL = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?token={TOKEN}"
    consultaWeb = req.get(URL)
    listaProduc = consultaWeb.json()
    return(listaProduc)

productos = consulta()




# print(productos['productos'][0]['nombre'])
# print(f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?token={TOKEN}")


ventana = Tk()
ventana.geometry("800x200")
ventana.title("Formulario Pedido")
miFrame= Frame(ventana)
miFrame.pack(fill="both")
texto1 = Label(miFrame, text="Ingrese Pedido")
texto1.grid(row=0, column=0)
texto1.config(font=('Arial', 12))

#-----Seccion de ID-----
id_label= Label(miFrame, text="ID:")
id_label.grid(row=1, column=0)
id_label.config(padx=10, pady=10)
cuadro_id=Entry(miFrame)
cuadro_id.grid(row=1, column=1)

#-----Seccion de Producto-----
apellido_label=Label(miFrame, text="Producto: ")
apellido_label.grid(row=2, column=0)
apellido_label.config(padx=10, pady=10)
cuadro_Producto= Entry(miFrame)
cuadro_Producto.grid(row=2, column=1)

#-----Seccion de Precio-----
apellido_label=Label(miFrame, text="Precio: ")
apellido_label.grid(row=3, column=0)
apellido_label.config(padx=10, pady=10)
cuadro_Precio= Entry(miFrame)
cuadro_Precio.grid(row=3, column=1)


#-----Boton Enviar------
def enviar():
    #messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")
    id = int(cuadro_id.get())
    name_prod = f"{productos['productos'][id]['nombre']}"
    name_prec = f"{productos['productos'][id]['precio']}"
    cuadro_Producto.delete(0,END)
    cuadro_Precio.delete(0,END)
    cuadro_Producto.insert(0,name_prod)
    cuadro_Precio.insert(0,name_prec)
   


btn1 = Button(miFrame, text="Enviar", command=enviar)
btn1.grid(column=0,row=10)


ventana.mainloop()