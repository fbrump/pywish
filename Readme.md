
# PyWish

The project that helps you to manage your wishes and collections like books, moves or wherever you want.

## Functions

* You can create a wishlist;
* You can manager the wishlist items;

## How to start

To run the project we just following the steps:

```
docker-compose down && docker-compose up -d
```

Next, create all migrations and apply they.

```
docker exec pywishapp python3 pywishproject/manage.py makemigrations

docker exec pywishapp python3 pywishproject/manage.py migrate
```

### Author

* Felipe Brum

### Mantainers

* 

### Stack

* Python 3
* Django
* PostgreSQL
* NginX
* unittest

#### Licence

GPL 2.0
