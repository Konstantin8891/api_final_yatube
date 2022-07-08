# API Yatube
API Yatube - API for the social network Yatube. Social network Yatube provides you ability for posting information including media files, following authors, commenting posts. Developed by Konstantin Vasilyev. Based on Django REST Framework 3.12.4. All dependecies are in requirements.txt.

89670253660@mail.ru

+79117836285 WhatsApp, Telegram

1. Clone project 

git clone git@github.com:Konstantin8891/api_final_yatube.git

2. cd api_final_yatube

3. Create virtual environment 

python -m venv env

or 

python3 -m venv venv

4. Activate virtual environment 

source venv/scripts/activate

or 

. venv/bin/activate

5. Upgrade pip 

python -m pip install --upgrade pip

6. Install all requirements 

pip install -r requirements.txt

7. Make migrations

python manage.py migrate

8. Run project

python manage.py runserver

9. Project Redoc

http://127.0.0.1:8000/redoc/

Project endpoints:

1. http://127.0.0.1:8000/api/v1/posts/

Requests - GET, POST
{
    "text": "string",
    "image": "string",
    "group": 0
}

Response:
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}

2. http://127.0.0.1:8000/api/v1/posts/{id}/

Requests - GET, PUT, PATCH, DELETE

{
    "text": "string",
    "image": "string",
    "group": 0
}

Response:
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}

3. http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Requests - GET, POST
{
    "text": "string"
}

Response:
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]

4. http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Requests - GET, PUT, PATCH, DELETE
{
    "text": "string"
}

Response:
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}

5. http://127.0.0.1:8000/api/v1/groups/

Request - GET

Response:
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]

6. http://127.0.0.1:8000/api/v1/groups/{id}/

Request - GET

Response:
{
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
}

7. http://127.0.0.1:8000/api/v1/follow/

Request - GET, POST
{
    "following": "string"
}

Response:
{
    "user": "string",
    "following": "string"
}

8. http://127.0.0.1:8000/api/v1/jwt/create/

Request - POST
{
    "username": "string",
    "password": "string"
}

Response:
{
    "refresh": "string",
    "access": "string"
}

9. http://127.0.0.1:8000/api/v1/jwt/refresh/

Request - POST
{
    "refresh": "string"
}

Response:
{
    "access": "string"
}

10. http://127.0.0.1:8000/api/v1/jwt/verify/

Request - POST
{
    "token": "string"
}

Response:
{
    "token": []
}
