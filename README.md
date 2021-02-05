El script fue desarrollado en python 3.9. y sistema operativo linux

-Instrucciones para la instalación y uso:

-Instalación:

- Tener una version de python 3 instalada.
- Instalar los requerimientos:
    -ir a la carpeta contenedora del proyecto y ejecutar desde la linea de comandos "pip install -r requirements.txt"

-Uso:

El script permite trabajar con 1 o varias consultas desde la linea de comandos para ello se habilitarón varios argumentos
-se: Seller es el numero de vendedor a consultar, ejemplo: -se 123456
-si: Site es el site a consultar, ejemplo: -si MLA
-m: Multiple, para usar esta funcion se debe mandar el argumento mas un "yes" y separar los datos mediante un .
    IMPORTANTE: en caso de multiple se debe respetara el orden de los argumentos 1ro seller 2do site
    ejemplo: -se 12345.45678.123 -si MLA.MLA.MLA -m yes


- Ejemplo uso simple:

    -1 Abrir una consola/terminal y dirigirse a la ubicación del archivo.
    -2 ejecutar el comando: python items_by_id.py -se 179571326 -si MLA.

    Si se desea ejecutar sin necesidad de escribir python se debe:
        dar permisos de ejecución al script
        - sudo chmod +x items_by_id.py
    -2.2 ejecutar ./items_by_id.py -se 179571326 -si MLA

- Ejemplo uso multiple:

    -1 Abrir una consola/terminal y dirigirse a la ubicación del archivo.
    -2 ejecutar el comando: python items_by_id.py -se 179571326.179571326 -si MLA.MLA -m yes

Para cada usuario consultado se creara un archivo de log, los campos estan separados por | para facilitar filtrados.
