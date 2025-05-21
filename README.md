para crear el proyecto:


Creamos una carpeta en el escritorio y navegamos a ella con powershell, o directamente abrimos powershell allí. 


Correremos estos los siguientes comandos en powershell como administrador (inicio, buscan powershell, click derecho abrir como administrador.


1. python -m venv venv

2. venv\Scripts\activate

En caso de que lance algun error: 

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 

y despues cerrar todas las ventanas de powershell


una vez activado debemos correr los siguientes comandos:

2. venv\Scripts\activate

3. pip install django
   
4. pip freeze > requirements.txt
   
5. django-admin startproject blog_de_viajes .
   
6. python manage.py startapp relatos
    
7. python manage.py migrate
    
8. python manage.py runserver
    
9. python manage.py createsuperuser


si clonas este repositorio, solo seria necesario correr todos hasta el 4o punto.
