from covid import *

def main():

    UrlCovidApi="http://api.covid19api.com/summary"

    datos = recuperarUrl(UrlCovidApi,"json")

    consulta = buscarPais("Argentina",datos)

    print(consulta)

if (__name__ == "__main__"):
	main()