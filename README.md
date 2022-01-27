# PruebaScrap

Scrapper of the first 5 pages of the search for "smartphones" in Mercadolibre of the Samsung brand that are in the Fulfillment (FULL) 

## Environment setup

-Install [python](https://www.python.org) *Select the option 'Add Python to PATH'*

-Install [xampp](https://www.apachefriends.org/es/index.html) *In the page 'Select Components' please select the component 'MySQL'*



## Development

### 1) Build the database

Start MySQL in xampp

Open Terminal and run the following instructions:
```
mysql -u root -p
Enter Password:
mysql>create database if not exists productos_prueba;
mysql>use productos_prueba;
mysql>$ CREATE TABLE `productos` (  `Id` int(11) NOT NULL AUTO_INCREMENT,  `Titulo` varchar(255) NOT NULL,  `Precio` varchar(255) NOT NULL,  `Reviews` varchar(100) NOT NULL,  `Fulfillment` varchar(100) DEFAULT NULL,  `Url` text,  PRIMARY KEY (`Id`));</code>
```

### 2) Install python modules 

Navigate to the project folder via terminal and run the following instructions:

Windows:

```
python get-pip.py
py -m pip install bs4
py -m pip install request
py -m pip install lxml
py -m pip install PyMySQL
```

MacOS:

```
python3 get-pip.py
python3 -m pip install bs4
python3 -m pip install request
python3 -m pip install lxml
python3 -m pip install PyMySQL
```

### 3) Execute

Navigate to the project folder via terminal and run the following instructions:

```python entregable.py```

Now you can see all the products in your database:

terminal
```
mysql -u root -p
*enter password*
use productos_prueba;
select * from productos; 
```
or this to better see the results:
```
select Titulo Titulo, Precio, Reviews from productos; //to better see the results 
```
Example of result:

![image](https://user-images.githubusercontent.com/98436887/151436725-b7deb3be-d3e3-4ec8-af51-61366bbf4e9b.png)





