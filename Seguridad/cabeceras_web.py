#!/usr/bin/env python3
#_*_ coding: utf8 _*_

# ----------------------------------------------------
# Muestra las cabeceras de respuesta de un sitio web
# cabereceras_web.py -t [url_sitio_web]
# ----------------------------------------------------

# Importación librerias
import requests
import argparse

# Definición de los posibles argumentos
parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t','--target',help='Ojetivo')
parser = parser.parse_args()


def main():
    # En el caso que se haya pasado el argumento con --target
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            cabeceras = dict(url.headers)
            for x in cabeceras:
                print(x + " : " + cabeceras[x])
        except:
            print("Fallo en la conexión")
    else:
        print("Falta definir el Objetivo")

# Llamada funcion principal
if __name__ == '__main__':
    try:
		main()
	except KeyboardInterrupt:
		print("Proceso detenido...")