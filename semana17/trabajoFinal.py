import requests as req
import os
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


raiz = Tk()
raiz.geometry("300x200")
raiz.title("Carga de Pedido")

miFrame= Frame()
miFrame.pack()

bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))

nombre_label= Label(miFrame, text="Cual es tu nombre:")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)
cuadro_nombre=Entry(miFrame)
cuadro_nombre.grid(row=1, column=1)

raiz.mainloop()