
# PyWish

The project that helps you to manage your wishes and collections like books, moves or wherever you want.

## Functions

* You can create a wishlist;
* You can manager the wishlist items;

### Use Case

* 

## How to start with docker-compose

To run the project we just following the steps:

```
docker-compose down && docker-compose up -d
```

Next, create all migrations and apply they.

```
docker exec pywishapp python3 pywishproject/manage.py makemigrations

docker exec pywishapp python3 pywishproject/manage.py migrate
```

## How to start with Docker

if you want just to run local with database, you can up the postgresql container with this command:

```
docker run --name pywish-postgresql -p 5031:5432 -e POSTGRES_DB=pywishdb -e POSTGRES_USER=pywishuser -e POSTGRES_PASSWORD=pywishpostgres -d postgres
```

Next, you start env of `pip` creating new env if not extis:

```
virtualenv env
```

And start the env if you use Windows execute this:

```
source env/Scripts/activate
```

If you use Linux execute this:

```
source env/bin/activate
```

Next, create all migrations and apply they.

```
python pywishproject/manage.py makemigrations

python pywishproject/manage.py migrate
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
