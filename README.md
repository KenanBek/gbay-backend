gBay-backend
============

Very simple Dajgno and REST Framework application with Product, Cart and CartItem models. Basically it is CRUD through admin interface and RESTful API. 

### Features

- products admin and API endpoint with list of products
- cart admin with inline items
- cart API endpoint with embedded items hyperlink (link to CartItem-detailed)
- cartitems API endpoint

Next:

- endpoint auth
- calculation of Product.amount based on closed carts (using signals)
- deploy to demo server and use in [gBay-mobile-web](https://github.com/KenanBek/gbay-mobile-web)

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
