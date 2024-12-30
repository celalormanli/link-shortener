# Link Shortener
The aim of this project is to convert the given links into shorter links and to direct the requests from the new links to the relevant links.
### Features
- Generating a 10 character link extension for the given link.
- Keeping the number of requests for shortened links.
- Redirecting requests from shortened links to original links.
### Structure 
- Django Framework and Django Rest Framework is used on Python.
- Relational database is used as database.
- Redis is used for caching.
- Api Key is used for Auth.
### Setup
- First add .env file in directory and fill like .env.examle
- Run Redis and set LOCATION for redis in settings.py
- install requirements.txt with
 ```sh
python3 -m pip install -r requirements.txt
```
- create super user with
```sh
 python3 manage.py createsuperuser
```
- run project with 
 ```sh
python3 manage.py runserver
```
### Usage
- Login and add api key with admin panel -> http://localhost:8000/admin/
- Link Building Api - POST -> http://localhost:8000/link/ 

        Add Api Key to Header
        Key -> Authorization
        Value -> Api-Key xxxx
        body -> {
            "main_link":"https://www.blabla.com"
        }

- Listing links Api - GET -> http://localhost:8000/link/

        Add Api Key to Header
        Key -> Authorization
        Value -> Api-Key xxxx
- Link redirecting - GET -> http://localhost:8000/zzzzz
