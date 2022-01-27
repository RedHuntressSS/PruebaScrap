# PruebaScrap

Scrapper of the first 5 pages of the search for "smartphones" in Mercadolibre of the Samsung brand that are in the Fulfillment (FULL) 

## Environment setup

-Install [python](https://www.python.org) *Select the option 'Add Python to PATH'*

-Install [xampp](https://www.apachefriends.org/es/index.html) *In the page 'Select Components' please select the component 'MySQL'*

-Install [MySQL Server y MySQL Workbench](https://dev.mysql.com/downloads/mysql/)


## Development

### 1) Build the database

Start MySQL in xampp

Terminal:
>mysql -u root -p
>
>*enter password*
>
>create database if not exists productos_prueba;
>
>use productos_prueba;
>
>CREATE TABLE `productos` (  `Id` int(11) NOT NULL AUTO_INCREMENT,  `Titulo` varchar(255) NOT NULL,  `Precio` varchar(255) NOT NULL,  `Reviews` varchar(100) NOT NULL,  `Fulfillment` varchar(100) DEFAULT NULL,  `Url` text,  PRIMARY KEY (`Id`));

### 2) Install python modules 

Navigate to the project folder via terminal and run the following instructions:

-python get-pip.py

-python3 -m pip install bs4

-py -m pip install request

-py -m pip install lxml

-py -m pip install PyMySQL

### 3) Execute

-python entregable.py

Now you can see all the products in your database:

terminal
>mysql -u root -p
>
>*enter password*
>
>use productos_prueba
>
>select * from productos
>

## License






