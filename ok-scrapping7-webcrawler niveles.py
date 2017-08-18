import requests
import re
from bs4 import BeautifulSoup
import time


def procesar_link(href, urls, archivo):
    # <a>Link</a> --> href == None
    # <a href="">Link</a> --> href == ""
    # <a href="#algo">Link</a> --> href == #algo

    # un metodo para que el debugger frene solo si aparece el link que estamos buscando
    if href != None and 'juggernaut-cargo-bikes-hauling-freight-and-pushing' in href:
        print(href)

    if href != None and href != "" and str(href)[0] not in ['#'] \
            and not href.startswith('whatsapp:') and not href.startswith('javascript:'):
        if href.startswith('/'):
            href = root_domain + href

        urls.append(href)
        print(href)
        archivo.write(href + '\n')

def obtener_links(url):
    try:
        response = requests.get(url)

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        content = soup.find('div', {'id': 'content'})
        if content:
            links_beautifulsoup = content.find_all('a')
        else:
            links_beautifulsoup = soup.find_all('a')

        # recorro todos los objetos de BS y armo una lista solo con los href (strings)
        links = set()
        for link in links_beautifulsoup:
            href = link.get('href')
            if href is not None:
                links.add(href)

        # busqueda de links por expresiones regulares
        links_regex = re.findall('"http[^"]*"', html)
        for link in links_regex:
            if link is not None:
                link_sin_comillas = link[1:-1]
                links.add(link_sin_comillas)

        return links
    except requests.exceptions.ConnectionError:
        return []


# se filtran links no deseados de acuerdo a una blacklist
def filtrar_links_no_deseados(links):
    blacklist = ['/login', '/signup']
    links_filtrados = []

    for link in links:
        hay_que_eliminar = False

        for blackitem in blacklist:
            if blackitem in link:
                hay_que_eliminar = True
                break

        if not hay_que_eliminar:
            links_filtrados.append(link)

    return links_filtrados

def esperar(segundos=1):
    time.sleep(segundos)


root_url = 'https://www.crunchbase.com/app/search/companies/7d363974ee8d53146f9558e7503049aa6f0572c2'
root_domain = 'https://www.crunchbase.com'
urls = []
archivo = open('urls.txt', 'w')

links = obtener_links(root_url)
esperar()

links_filtrados = filtrar_links_no_deseados(links)

# links en la pagina raiz
for link in links_filtrados:
    procesar_link(link, urls, archivo)

separador = "------ Termino de recorrer la raiz ------"
print(separador)
archivo.write(separador + '\n')


# se recorre links de la raiz
for url in urls:
    links = obtener_links(url)
    if len(links) == 0:
        espera = 90
        print('Ocurrio un requests.exceptions.ConnectionError, se esperaran {} segundos...'.format(espera))
        time.sleep(espera)

        # reintento obtener los links
        links = obtener_links(url)

    esperar()

    links_filtrados = filtrar_links_no_deseados(links)

    # links en las paginas de primer nivel de profundidad
    for link in links_filtrados:
        procesar_link(link, urls, archivo)

archivo.close()
