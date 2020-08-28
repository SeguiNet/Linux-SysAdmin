#!/usr/bin/env python3

# ----------------------------------------------------
# Extrae a un fichero la lista de href de una pagina web
# 
# ----------------------------------------------------

from bs4 import BeautifulSoup
import urllib3

# Funcion extraccion nombre plugins
def getLinks(url):
    archivo = open("lista_plugins.txt","w")

    # Generamos la peticion a la pagina web
    http = urllib3.PoolManager()
    http.headers = {'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data,'html.parser')

    # Buscamos todas las etiquetas a y extraemos href
    for link in soup.findAll('a'):
        archivo.write(link.get('href'))
        archivo.write("\n")
    
    archivo.close()

getLinks("https://plugins.svn.wordpress.org/")


