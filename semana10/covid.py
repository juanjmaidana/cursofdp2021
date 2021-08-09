#Librerias
import requests
import time
import json

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

def convertirFecha(cadenaFecha):
    
    formato = "%Y-%m-%dT%H:%M:%S"
    fecha = time.strptime(cadenaFecha[0:19], formato)
    fechaConvertida = f"Fecha de actualización:  {fecha.tm_mday}/{fecha.tm_mon}/{fecha.tm_year} a las {fecha.tm_hour}:{fecha.tm_min}"

    return fechaConvertida

def escribirJSON(file):
    
   with open('semana10\covid_arg.json', 'w') as outfile:
       json.dump(file, outfile)

def imprimirPantalla(consulta,fechaAct):
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

