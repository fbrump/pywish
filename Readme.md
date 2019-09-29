
# PyWish

The project that helps you to manage your wishes and collections like of things you want.

## Functions

* You can create a wishlist;
* You can manager the wishlist items;

### Use Case

* The user can create a wish list;
* The user cannot create two or more wish lists with the same name;
* The user can update wish list name and description;
* The user can turn on or off the wishl list;
* The user can list all wish lists;
* The user can create items in wish list;
* The user cannot create more then one item with the same name and code;
* The user can list all items from one wish list;
* The user can turn on or off one item;
* The user can update item code (external code), name and description;

## How to start with docker-compose

To run the project we just following the steps:

``` yml
docker-compose down && docker-compose up -d
```

Next, create all migrations and apply they.

``` yml
docker exec pywishapp python3 pywishproject/manage.py makemigrations

docker exec pywishapp python3 pywishproject/manage.py migrate
```

Finelly you can acess this url:

```text
    http://localhost:8992
```

## How to start with Docker

if you want just to run local with database, you can up the postgresql container with this command:

```yml
docker run --name pywish-postgresql -p 5031:5432 -e POSTGRES_DB=pywishdb -e POSTGRES_USER=pywishuser -e POSTGRES_PASSWORD=pywishpostgres -d postgres
```

Next, you start env of `pip` creating new env if not extis:

```bash
virtualenv env
```

And start the env if you use Windows execute this:

```bash
source env/Scripts/activate
```

If you use Linux or MacOS execute this:

```bash
source env/bin/activate
```

Next, create all migrations and apply they.

```python
python pywishproject/manage.py makemigrations

python pywishproject/manage.py migrate
```

### Author

* Felipe Brum

### Mantainers

* ..

### Stack

* Python 3
* Django
* PostgreSQL
* NginX
* unittest
* Docker
* docker-compose

#### Licence

GPL 2.0
