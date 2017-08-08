import requests
from bs4 import BeautifulSoup


def procesar_link(href, urls, archivo):
    if href != None and str(href)[0] not in ['#']:
        if href.startswith('/'):
            href = root_domain + href

        urls.append(href)
        print(href)
        archivo.write(href + '\n')

def obtener_links(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    content = soup.find('div', {'id': 'content'})
    if content:
        links = content.find_all('a')
    else:
        links = soup.find_all('a')

    return links


root_url = 'https://es.wikipedia.org/wiki/Bicicleta_plegable'
root_domain = 'https://es.wikipedia.org'
urls = []
archivo = open('urls.txt', 'w')

links = obtener_links(root_url)

# links en la pagina raiz
for link in links:
    href = link.get('href')
    procesar_link(href, urls, archivo)

separador = "------ Termino de recorrer la raiz ------"
print(separador)
archivo.write(separador + '\n')


# se recorre links de la raiz
for url in urls:
    links = obtener_links(url)

    # links en las paginas de primer nivel de profundidad
    for link in links:
        href = link.get('href')
        procesar_link(href, urls, archivo)

archivo.close()