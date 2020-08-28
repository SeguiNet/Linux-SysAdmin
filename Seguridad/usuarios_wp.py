#!/usr/bin/env python3
#_*_ coding: utf8 _*_

# ----------------------------------------------------
# Muestra los usuarios de una web con WordPress
# usuarios_wp.py -t [dominio]
# ----------------------------------------------------

import json
import argparse
import requests

# Definición de los posibles argumentos
parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t','--target',help='Dominio')
parser = parser.parse_args()

def main():
    try:
        if parser.target:
            url = "https://"+parser.target+"/wp-json/wp/v2/users/"
            response = requests.get(url)
            for u in response.json():
                user = u['slug']
                print(user)
        else:
            print("ERROR: Falta el parametro de URL")
    except:
        print("ERROR: Dominio incorrecto")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()