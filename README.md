# Proyecto-programacion-pizzeria

1 Introduccion:

Este proyecto es la gestion de una pizzeria junto a sus ofertas, precios y cambios de temporadas

2 Como descargar el proyecto:

Ir a github a este link https://github.com/Alexnegre05/Proyecto-programacion-pizzeria.git,
desde aqui puedes clicar en el boton code y en el desplegable puedes descargar el achivo de el proyecto .zip clicando en la opcion download zip

necesitas descomprimir el archivo .zip una vez hecho este proceso necesitaras un programa para poder ejecutar el codigo un editor de codigo, se recomienda visual studio code, la version mas reciente, se puede instalar desde este link https://code.visualstudio.com/download pero se puede instalar otros editores de codigo que permitan python 3.14

escoge que opcion descargar dependiendo de el tipo de sistema operativo que tengas

para finalizar necesitaras instalar python ir a download https://www.python.org/downloads/ en este link y buscar la version 3.14
que es la version de python en la que se ha hecho este programa


3 Estructura de el proyecto y ejecutable:

El proyecto tiene un main.py donde se ejecuta el codigo, solo ejecutar ese archivo para probar el programa.

Aparte de main hay un src donde esta todo el codigo y dentro hay dos carpetas datos y modulos y un archivo menu.


4 Explicacion contenido en los archivos:


4.1 Archivo Principal: 

Main se encarga de gestionar la llamada a otros menus, es el programa principal

4.2 menus.py 


En menu se encuentra las funciones de los menus y submenus 

se encarga de pedir a el usuario que quiere hacer y llamar a las funciones pertinentes de las otras 2 carpetas


4.3 Carpeta Datos:

En la carpeta datos hay un archivo init junto a otros 4 archivos, que contienen cada uno

bebidas.py contiene un diccionario de nombre bebida-precio con 6 bebidas y el precio correspondiente
 
pizza.py contiene las 20 pizzas en formato diccionario nombre pizza-ingredientes donde los ingredientes es una lista,
ingredientes-gramos y gramo-precio asi como una lista temporadas con un solo valor 1 0.5 o 1.5 que indica el modificador que se le va a a hacer a los precios.


4.4 carpeta Modulos:


4.4.1 calculo de la pizza: 

Para modulos hay un calculo.py que se encarga de el precio de la pizza para ello se calcula precio ingredientes usando gramos ingredientes*precio por gramo.

se le suman los suministros aproximados calculamos un porcentaje de esos gastos totales al final de el mes que se distribuyen a la pizza asi como una suma de beneficioa a la pizza.

para finalizar se le suma el iva a el precio final.


4.4.2 otros ficheros de modulos:

cambiar temporada es un archivo que sirve para que el usuario escriba que temporada quiere cambiar dependiendo de la temporada actual va a mostrar un menu u otro pero la logica no varia casi nada.

catalogo productos sirve para que el usuario en el menu pueda ver un desplegable de las pizzas junto a sus ingredientes.

pedidos lista todos los productos que ha puesto el usuario independientemente de si son bebidas o pizzas.

los productos se añaden a el carrito en el mismo instante en el que el usuario ha seleccionado una pizza o una bebida.

seleccionar pizza o bebida controlan a el usuario que opcion quiere y si es correcta o no.

4.4.3 ofertas:

por ultimo las ofertas hay 3, la primera es  2 pizzas y solo 2 pizzas donde incluimos 1 bebida gratuita, para ello se incluye una bebida y se modifica el precio para que sea 0.

La segunda es de 4 pizzas y solo 4 pizzas se aplica un descuento de 5%  en el precio total
y finalmente una ultima oferta que si y solo si tienes mas o igual de 5 bebidas y pizzas en conjunto y menso de 20 se te aplica un x porcentaje sumando el numero de pizzas y bebidas


Creadores = Alex Negre, Andres Ponce
