from covid import *

def main():

    UrlCovidApi="http://api.covid19api.com/summary"

    datos = recuperarUrl(UrlCovidApi,"json")

    consulta = buscarPais("Argentina",datos)

    fecha=f"{datos['Date']}"
   
    fechaAct=convertirFecha(fecha)

    escribirJSON(consulta)

    print("DATOS COVID ARGENTINA")
    print("-----------------------------------")
    print(f"Nuevos Confirmado {consulta['NuevosConfirmados']}")
    print(fechaAct)

    print(consulta)

if (__name__ == "__main__"):
	main()