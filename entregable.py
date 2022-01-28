#Scrapper de las 5 primeras páginas de la búsqueda.
#Almacenar los productos normalizados en una tabla de base de datos relacional a preferencia del desarrollador

from bs4 import BeautifulSoup
import requests

productos=[]

def scrapPagina(url, marca):
    #función que realiza el scrap de la url indicada en busqueda de los articulos de la marca especificada que estan en Fulfillment
    #Retorna el numero de productos encontrados y los almacena en la lista productos

    p=requests.get(url)
    p.status_code
    s= BeautifulSoup(p.text, 'lxml')
    resultados=s.find('ol', attrs={'class': 'ui-search-layout ui-search-layout--stack'}).find_all('li', attrs={'class': 'ui-search-layout__item'})
    cont=0
    for resultado in resultados:
        re2=BeautifulSoup(str(resultado), 'lxml')
        re3=re2.find('svg', attrs={'class': 'ui-search-icon ui-search-icon--full'})
        re4=re2.find('div', attrs={'class': 'ui-search-item__group ui-search-item__group--title'})
        titulo=re4.a.get('title')
        if re3!=None and marca.upper() in titulo.upper():
            cont+=1
            productos.append(extraerDatosProducto(re2, 'yes', titulo))
    return cont

def scrap(url, marca, num):
    #Funcion que llama a la función scrapPaginas de acuerdo a la cantidas de paginas en las que se necesita realizar la busqueda desde el url indicado

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


#Almacenar los productos normalizados en una tabla de base de datos relacional a preferencia del desarrollador

def extraerDatosProducto(re2, full, titulo):
    #función que extrae los atributos normalizados de los productos 
    #retorna los datos de un producto en formato JSON
    re5=re2.find('span', attrs={'class': 'price-tag-symbol'})
    re5_1=re2.find('span', attrs={'class': 'price-tag-fraction'})
    re6=re2.find('span', attrs={'class': 'ui-search-reviews__amount'})
    url=re2.a.get('href')           
    if re5 and re5_1:
        precio=re5.text+re5_1.text
    else:
        precio='Null'       
    if re6:
        reviews=re6.text
    else:
        reviews='Null'
    producto={
        "Titulo": titulo,
        "Precio": precio,
        "Reviews": reviews,
        "Fulfillment": full,
        "Url": url
    }
    return producto  


def almacenarProductosBD(productos):
    #funcion que almacena los productos en la base de datos
    import pymysql

    connection= pymysql.connect(
        host='localhost',
        user='root',
        port='',
        password='LSVG1531',#Escriba aqui su contraseña en caso de ser necesario
        db='productos_prueba'
    )

    cursor= connection.cursor()

    sqlRegistros="select count(*) from productos"
    cursor.execute(sqlRegistros)
    registros=cursor.fetchone()
    r1=int(registros[0])

    for producto in productos:
        sql=sql="INSERT INTO productos(Titulo, Precio, Reviews, Fulfillment, Url) VALUES('"+producto['Titulo']+"', '"+producto['Precio']+"', '"+producto['Reviews']+"', '"+producto['Fulfillment']+"','"+producto['Url']+"')"
        #print(str(sql))
        cursor.execute(str(sql))
        connection.commit()

    cursor.execute(sqlRegistros)
    registros=cursor.fetchone()
    r2=int(registros[0])

    return r2-r1

def main():
    url='https://listado.mercadolibre.com.ar/celular-smarphones#D[A:celular%20smarphones]'
    marca='Samsung'
    paginas=5
    Totales=scrap(url, marca, paginas)
    print("La cantidad de productos encontrados de la marca ", marca, " que están en el Fulfillment, en los resultados de las ", paginas, " primeras paginas es: ", sum(Totales))
    almacenarProductosBD(productos)

main()