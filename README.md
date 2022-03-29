# api_final
api final yatube

1. Clone project 
git clone git@github.com:Konstantin8891/api_final_yatube.git
cd api_final_yatube
2. Create virtual environment 
python -m venv env
3. Activate virtual environment 
source venv/scripts/activate
4. Upgrade pip 
python -m pip install --upgrade pip
5. Install all requirements 
pip install -r requirements.txt
6. Make migrations
python manage.py migrate
7. Run project
python manage.py runserver
