from bs4 import BeautifulSoup
import requests

def scrapPagina(url, marca):
    p=requests.get(url)
    p.status_code
    s= BeautifulSoup(p.text, 'lxml')
    resultados=s.find('ol', attrs={'class': 'ui-search-layout ui-search-layout--stack'}).find_all('li', attrs={'class': 'ui-search-layout__item'})
    cont=0
    for resultado in resultados:
        re2=BeautifulSoup(str(resultado), 'lxml')
        re3=re2.find('svg', attrs={'class': 'ui-search-icon ui-search-icon--full'})
        re4=re2.find('div', attrs={'class': 'ui-search-item__group ui-search-item__group--title'})
        if re3!=None and marca.upper() in re4.a.get('title').upper():
            cont+=1
    return cont

def scrapPaginas(url, marca, num):
    Totales=[]
    for i in range(num):
        print(url)
        Totales.append(scrapPagina(url, marca))
        p=requests.get(url)
        p.status_code
        s= BeautifulSoup(p.text, 'lxml')
        s1=s.find('li', attrs={'class':'andes-pagination__button andes-pagination__button--next'})
        url=s1.a.get('href')
    return Totales

Totales=scrapPaginas('https://listado.mercadolibre.com.ar/celular-smarphones#D[A:celular%20smarphones]', 'samsung', 5)
print(Totales)