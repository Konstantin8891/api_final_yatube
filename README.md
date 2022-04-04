# api_final
API final Yatube - API for the social network Yatube. Social network Yatube provides you ability for posting information including media files, following post author, commenting posts. Developed by Konstantin Vasilyev.


1. Clone project 
git clone git@github.com:Konstantin8891/api_final_yatube.git
2. cd api_final_yatube
3. Create virtual environment 
python -m venv env
4. Activate virtual environment 
source venv/scripts/activate
5. Upgrade pip 
python -m pip install --upgrade pip
6. Install all requirements 
pip install -r requirements.txt
7. Make migrations
python manage.py migrate
8. Run project
python manage.py runserver
Project endpoints:
1. http://127.0.0.1:8000/api/v1/posts/
Requests - GET, POST
{
"text": "string",
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
3. http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Requests - GET, POST
{
"text": "string"
}
4. http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
Requests - GET, PUT, PATCH, DELETE
{
"text": "string"
}
5. http://127.0.0.1:8000/api/v1/groups/
Request - GET
6. http://127.0.0.1:8000/api/v1/groups/{id}/
Response - GET
7. http://127.0.0.1:8000/api/v1/follow/
Request - GET, POST
{
"following": "string"
}
8. http://127.0.0.1:8000/api/v1/jwt/create/
Request - POST
{
"username": "string",
"password": "string"
}
9. http://127.0.0.1:8000/api/v1/jwt/refresh/
Request - POST
{
"refresh": "string"
}
10. http://127.0.0.1:8000/api/v1/jwt/verify/
Request - POST
{
"token": "string"
}
