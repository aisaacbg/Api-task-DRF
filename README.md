# Api-task-DRF
Api task DRF

- Pasos para la instalación de ambiente local
1. Instalar Docker
2. Clonar este repositorio
3. Abrir terminar y dirigirte a la carpeta de este repositorio en tu computadora.

4. Ejecutar:
  docker-compose build

5. Ejecutar:
  docker-compose exec apitasks python manage.py makemigrations

6. Ejecutar:
docker-compose exec apitasks python manage.py migrate

7. Ejecutar:
docker-compose up

Una vez completado esas instrucciones podrás ingresar a la url http://0.0.0.0:8000/api/task
https://raw.githubusercontent.com/aisaacbg/Api-task-DFR/apitask/principal.png

Agregar información a la base de datos mediante endpoint:
ingresar a la siguiente url desde su terminal: curl http://0.0.0.0:8000/endpoint/  
Desde su navegador http://0.0.0.0:8000/endpoint/

Ejecutar desde la terminal: curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/task/
Devolvera la información en formato json 

Ó bien si utiliza un cliente como Postman agregar la url http://0.0.0.0:8000/api/task y obtendra la información en formato json

Obtener tareas mediante por query string ejemplo: http://0.0.0.0:8000/api/task/?q='Fi'

Ver la información de una tarea mediante id http://0.0.0.0:8000/api/task/'id_de_tarea'

Listar por tareas completadas http://0.0.0.0:8000/api/completadas

Listar por tareas completadas http://0.0.0.0:8000/api/pendientes


Agregar la url http://0.0.0.0:8000/api/xml para obtener la información en formato xml








