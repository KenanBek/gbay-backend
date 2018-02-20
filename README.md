gBay-backend
============

### Setup

    virtualenv env
    .\env\scripts\activate
    pip install -r requirements.txt
    
### Run

    cd gbay
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### Usage

Administration: http://localhost:8000/admin

API: http://localhost:8000/api
