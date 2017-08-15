import requests
import re
from bs4 import BeautifulSoup


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
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    content = soup.find('div', {'id': 'content'})
    if content:
        links_beautifulsoup = content.find_all('a')
    else:
        links_beautifulsoup = soup.find_all('a')

    # recorro todos los objetos de BS y armo una lista solo con los href (strings)
    links = []
    for link in links_beautifulsoup:
        href = link.get('href')
        links.append(href)

    # busqueda de links por expresiones regulares
    links_regex = re.findall('"http[^"]*"', html)
    for link in links_regex:
        link_sin_comillas = link[1:-1]
        links.append(link_sin_comillas)

    return links


root_url = 'https://www.kickstarter.com/discover/advanced?term=Bikes&woe_id=0&sort=magic&seed=2504144&page=1'
root_domain = 'https://www.kickstarter.com'
urls = []
archivo = open('urls.txt', 'w')

links = obtener_links(root_url)

# links en la pagina raiz
for link in links:
    procesar_link(link, urls, archivo)

separador = "------ Termino de recorrer la raiz ------"
print(separador)
archivo.write(separador + '\n')


# se recorre links de la raiz
for url in urls:
    links = obtener_links(url)

    # links en las paginas de primer nivel de profundidad
    for link in links:
        procesar_link(link, urls, archivo)

archivo.close()
