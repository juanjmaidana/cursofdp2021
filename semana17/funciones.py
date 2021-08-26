import requests as req
from tkinter import *
from tkinter import messagebox
#import os from dotenv import load_dotenv

SERVIDOR = "http://pad19.com:3030"
ENDPOINT_PRODUCTOS = "productos/10"
ENDPOINT_PEDIDOS = "pedidos/10"
ENDPOINT_CONSULTA_PEDIDOS = "pedidos/"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgiLCJub21icmUiOiJKdWFuIE1haWRhbmEifQ.Iv6XfvzwAGlo1mw-LoWC3l5bKeW4itVfhy8GMxPTwCE"
URL_TELEGRAM = "https://api.telegram.org/bot"
TOKEN_TELEGRAM = "1943297231:AAGSMdz6yKqvzrNSgo8IVhq9vvBqIzvbzrE"
ENDPOINT_TELEGRAM = "sendMessage"
ID_CHAT = "1633210210"#"-559723042"


def consulta():
    URL = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?token={TOKEN}"
    consultaWeb = req.get(URL)
    listaProduc = consultaWeb.json()
    return(listaProduc)

def gui_pricipal(productos):
    #-----GUI---------
    ventana = Tk()
    ventana.geometry("400x300")
    ventana.title("Formulario Pedido")
    miFrame= Frame(ventana)
    miFrame.pack(fill="both")
    texto1 = Label(miFrame, text="Pedido")
    texto1.grid(row=0, column=0)
    texto1.config(font=('Arial', 12))

    #-----Seccion de ID-----
    id_label= Label(miFrame, text="ID:")
    id_label.grid(row=1, column=0,sticky='w')
    id_label.config(padx=10, pady=10)
    cuadro_id=Entry(miFrame)
    cuadro_id.place(x=40,y=35)

    #-----Seccion de Producto-----
    producto_label=Label(miFrame,text="Producto:  ")
    producto_label.grid(column=0,row=2,sticky='w')
    producto_label.config(padx=10, pady=10)

    #-----Seccion de Precio-----
    precio_label=Label(miFrame, text="Precio: ")
    precio_label.grid(column=0,row=3,sticky='w')
    precio_label.config(padx=10, pady=10)

    #-----Seccion de Stock-----
    stock_label=Label(miFrame, text="Stock: ")
    stock_label.grid(column=0,row=4,sticky='w')
    stock_label.config(padx=10, pady=10)

    #-----Seccion de Pedido-----
    pedido_label=Label(miFrame, text="Ingrese su Pedido: ")
    pedido_label.grid(column=0,row=5,sticky='w')
    pedido_label.config(padx=10, pady=10)
    cuadro_pedido=Entry(miFrame)
    cuadro_pedido.place(x=120,y=188)

    def cargar():
        #messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")
        id = int(cuadro_id.get())
        name_prod = f"Producto: {productos['productos'][id]['nombre']}"
        name_prec = f"Precio:  {productos['productos'][id]['precio']}"
        name_stock = f"Stock:  {productos['productos'][id]['stock']}"
        
        producto_label.config(text=name_prod)
        precio_label.config(text=name_prec)
        stock_label.config(text=name_stock)

    def agregar():
        id = int(cuadro_id.get())
        cant = int(cuadro_pedido.get())
        stock = productos['productos'][id]['stock']
        pedido = {"id":id,"pedido":cant}
        if (cant > stock):
             messagebox.showinfo(message="STOCK INSUFICIENTE", title="ERROR")
        else:
            URL_PEDIDO = f"{SERVIDOR}/{ENDPOINT_PEDIDOS}?token={TOKEN}"
            pedidoPost = req.post(URL_PEDIDO,pedido)
            ordenPedido = pedidoPost.json()
            mensajePedido = f"{ordenPedido['mensaje']} con el número de orden: {ordenPedido['codigo']}"
            telegramURL = f"{URL_TELEGRAM}{TOKEN_TELEGRAM}/{ENDPOINT_TELEGRAM}"
            telgramSend = req.post(telegramURL,data={'chat_id':ID_CHAT,'text': mensajePedido})
            messagebox.showinfo(message=mensajePedido, title="Pedido Registrado")
            messagebox.showinfo(message=telgramSend.status_code, title="Telegram")


    #-----Boton Cargar------
    btn1 = Button(miFrame, text="Cargar", command=cargar)
    btn1.place(x=160,y=30)

    #-----Boton Agregar al Pedido------
    btn2 = Button(miFrame, text="Agregar al Pedido", command=agregar)
    btn2.place(x=180,y=188)




    ventana.mainloop()




