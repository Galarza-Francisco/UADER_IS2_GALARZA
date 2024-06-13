# TP N° 6 Ingenieria de Software II


## Resolucion de Trabajo Practico N°6

## Punto 2
### a-descarga de carpeta scr desde campus
- b ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/22825c9d-c342-46c0-b4d8-29bf26668c8b)

    1° ejecuto el codigo segun la documentacion con el archivo getJason-2.7 
    2° archivos involucrados getJason2.7.pyc , sitedata.json.
    3° se leen los parametros de ingreso del programa.
       se abre el json y se lee.
       se almacena los datos obtenidos.
       se devuelve el valor al usuario. 
    4° componentes: archivo json, archivo getJason, token, datos 

- d ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/664164d0-c6dd-4b14-906b-c2b24687c035)

- e ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/0f4cb2eb-e8e4-4a37-bef9-7c9be7fb08f8)

- f los errores que obtengo en el nuevo getJason son porque entre version cambio la forma en el que se declaran algunas cosas:
   los print son una funcion asi que necesitan llevar parentesis.
   la asignacion de str no es necesaria en esta nueva version para hacer el print
   la función open devuelve un objeto de tipo texto en lugar de bytes, por lo que no es necesario decodificar los datos leídos del archivo.
   En Pla nueva version sys.argv devuelve una lista de cadenas Unicode en lugar de bytes, por lo que no es necesario realizar ninguna conversión.  
- g generando un nuevo archivo llamado getJasonNew.py, modificando lo correspondiente obtengo el mismo resultado ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/cc1bd040-544d-4e77-8597-a32fa0a017e0)

- h comprobando funcionamiento con dos versiones actuales de python 3.10 y 3.11
![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/69eb01d0-436a-4417-aca6-42166eca70f0)

- j ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/b03d30d5-ad19-46e7-bc15-95d5527223ee)

- k verifica y valida correctamente el valor del token.
### Punto 3
- g 
![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/113522d1-cf87-426f-b8a8-a4ce9c45435d)

### Punto 4

- b ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/b58b7961-0499-45d4-9cc1-18ee48ca06e8)

- d  ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/fc5a895a-03f3-4647-9297-9c8160cd088f)

- e error por falta de saldo:  ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/d3d40492-f3b6-465f-a8aa-b42931912c17) 

- f ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/00136e8c-f012-43a9-a5a9-b3ffc532b0bb)

- h ![image](https://github.com/Galarza-Francisco/UADER_IS2_GALARZA/assets/91553669/84c2656d-c9fc-4cb5-8a2d-2538032fb4ca)
   


## Docentes de Cátedra

Este curso esta a cargo del Profesor:
- Dr. Pedro E. Colla

## Herramientas usadas
uncompyle6
pylint
python3.6
python2.7
python3.10
python3.11
Este archivo esta construido en base a [GitHub Docs](https://docs.github.com/).

