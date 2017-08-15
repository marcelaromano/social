import requests
from bs4 import BeautifulSoup


 # es igual al scrapping 1 pero itera sobre una lista de url y me las tira todas juntas en un archivo .. diferencias abro y cierro el archvo solo una vez y saco la url definida
# url = "https://es.wikipedia.org/wiki/Bicicleta_plegable"
archivo_salida = open('soup_salida.txt', 'w')

# lista_url=['http://www.lanacion.com.ar/comunidad-de-negocios','https://es.wikipedia.org/wiki/Dom%C3%B3tica','https://en.wikipedia.org/wiki/Folding_bicycle','https://en.wikipedia.org/wiki/Electric_bicycle','http://calzadoparati.com/']
#lista[0:10]
# Ejemplo de contenido de archivo urls.ytxt: ['http://servicios.lanacion.com.ar/solo-texto\n', 'http://www.lanacion.com.ar/comunidad-de-negocios\n']
archivo_urls = open('urls.txt')
lista_url = archivo_urls.readlines()
archivo_urls.close()

for url in lista_url:
    # corto por el  el barrra n y me quedo con el de la iz. poque el de la der es vacio
    url = url.split('\n')[0]
    print('Procesando {}'.format(url))

    try:
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        for p in soup.find_all('p'):
            contenido = p.text
            if contenido != "":
                print(contenido)
                archivo_salida.write(contenido + '\n')
    except:
        print('Error con la URL: {}'.format(url))

archivo_salida.close()