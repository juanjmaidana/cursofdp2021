#Librerias
import requests

#funciones
def recuperarUrl(destino,formato):
    consulta = requests.get(destino)

    if (consulta):
        if (consulta.status_code == 200):
            if (formato == "original"):
                return consulta.content
            elif (formato == "texto"):
                return consulta.text
            elif (formato == "json"):
                return consulta.json()
            else:
                return False
        elif (consulta.status_code == 429):
            print ("Demasiadas solicitudes por minuto")
            return False
        else:
            print(f"ERROR al recuperar contenidos: {consulta.message}")
            return False
    else:
        print("ERRROR general en la solicitud")

def buscarPais(consulta,origenDatos):
    i=-1
    for f in origenDatos['Countries']:
        i=i+1
        pais=f"{origenDatos['Countries'][i]['Country']}"

        NuevosConfirmados=f"{origenDatos['Countries'][i]['NewConfirmed']}"
        TotalConfirmados=f"{origenDatos['Countries'][i]['TotalConfirmed']}"
        NuevasMuertes=f"{origenDatos['Countries'][i]['NewDeaths']}"
        TotalMuertes=f"{origenDatos['Countries'][i]['TotalDeaths']}"
        NuevosRecuperados=f"{origenDatos['Countries'][i]['NewRecovered']}"
        TotalRecuperados=f"{origenDatos['Countries'][i]['TotalRecovered']}"
        


        if pais==consulta :
            consultaDic={}
            consultaDic = {'pais':pais,'NuevosConfirmados':NuevosConfirmados,'TotalConfirmados':TotalConfirmados,'NuevasMuertes':NuevasMuertes,'TotalMuertes':TotalMuertes,'NuevosRecuperados':NuevosRecuperados,'TotalRecuperados':TotalRecuperados}
            return consultaDic
            