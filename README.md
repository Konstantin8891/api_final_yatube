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
9. Now you're able to see examples of requests for my API at 
http://127.0.0.1:8000/redoc/
