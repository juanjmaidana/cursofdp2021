from covid import *

def main():

    UrlCovidApi="http://api.covid19api.com/summary"

    datos = recuperarUrl(UrlCovidApi,"json")

    consulta = buscarPais("Argentina",datos)

    fecha=f"{datos['Date']}"
   
    fechaAct=convertirFecha(fecha)

    escribirJSON(consulta)

    print("-------------------------------------------------------")
    print("DATOS COVID ARGENTINA")
    print("-------------------------------------------------------")
    print(f"Nuevos Confirmado: {consulta['NuevosConfirmados']}")
    print(f"Total de Confirmado: {consulta['TotalConfirmados']}")
    print(f"Nuevas Muertes: {consulta['NuevasMuertes']}")
    print(f"Total de Muertes: {consulta['TotalMuertes']}")
    print(f"Nuevos Recuperados: {consulta['NuevosRecuperados']}")
    print(f"Total de Recuperados: {consulta['TotalRecuperados']}")
    print("-------------------------------------------------------")
    print(fechaAct)
    print("-------------------------------------------------------")
    #print(consulta)

if (__name__ == "__main__"):
	main()
