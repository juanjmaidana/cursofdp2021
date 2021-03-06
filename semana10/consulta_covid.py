from covid import *

def main():

    UrlCovidApi="http://api.covid19api.com/summary"

    datos = recuperarUrl(UrlCovidApi,"json")

    consulta = buscarPais("Argentina",datos)

    fecha=f"{datos['Date']}"
   
    fechaAct=convertirFecha(fecha)

    escribirJSON(consulta)

    imprimirPantalla(consulta,fechaAct)

    porcentaje(datos,consulta)


if (__name__ == "__main__"):
	main()
