#Scrapper de las 5 primeras páginas de la búsqueda.

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
        #print(url)
        Totales.append(scrapPagina(url, marca))
        p=requests.get(url)
        p.status_code
        s= BeautifulSoup(p.text, 'lxml')
        s1=s.find('li', attrs={'class':'andes-pagination__button andes-pagination__button--next'})
        url=s1.a.get('href')
    return Totales


url='https://listado.mercadolibre.com.ar/celular-smarphones#D[A:celular%20smarphones]'
marca='Samsung'
paginas=5
#Totales=scrapPaginas(url, marca, paginas)
#print(Totales)
#print("La cantidad de productos encontrados de la marca ", marca, " que están en el Fulfillment, en los resultados de las ", paginas, " primeras paginas es: ", sum(Totales))

#Almacenar los productos normalizados en una tabla de base de datos relacional a preferencia del desarrollador

def almacenarProductos(url):
    productos=[]
    p=requests.get(url)
    p.status_code
    s= BeautifulSoup(p.text, 'lxml')
    resultados=s.find('ol', attrs={'class': 'ui-search-layout ui-search-layout--stack'}).find_all('li', attrs={'class': 'ui-search-layout__item'})
    for resultado in resultados:
        re2=BeautifulSoup(str(resultado), 'lxml')
        re3=re2.find('svg', attrs={'class': 'ui-search-icon ui-search-icon--full'})
        re4=re2.find('div', attrs={'class': 'ui-search-item__group ui-search-item__group--title'})
        re5=re2.find('span', attrs={'class': 'price-tag-symbol'})
        re5_1=re2.find('span', attrs={'class': 'price-tag-fraction'})
        re6=re2.find('span', attrs={'class': 'ui-search-reviews__amount'})
        if re4.a.get('title'):
            titulo=re4.a.get('title')
        else:
            titulo='Null'
            
        if re5 and re5_1:
            precio=re5.text+re5_1.text
        else:
            precio='Null'
        
        if re6:
            reviews=re6.text
        else:
            reviews='Null'
        if re3!=None:
            full='yes'
        else:
            full='no'
        producto={
            "Titulo": titulo,
            "Precio": precio,
            "Reviews": reviews,
            "Fulfillment": full
        }
        productos.append(producto)
    return productos

productos=almacenarProductos('https://listado.mercadolibre.com.ar/celular-smarphones#D[A:celular%20smarphones]')
print(productos)

def productosBD(productos):
    import pymysql

    connection= pymysql.connect(
        host='localhost',
        user='root',
        password='LSVG1531',
        db='productos_prueba'
    )

    cursor= connection.cursor()

    for producto in productos:
        sql=sql="INSERT INTO productos(Titulo, Precio, Reviews) VALUES('"+producto['Titulo']+"', '"+producto['Precio']+"', '"+producto['Reviews']+"')"
        cursor.execute(str(sql))
        connection.commit()

productosBD(productos)