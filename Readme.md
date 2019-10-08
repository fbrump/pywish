[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.svg?v=103)](https://opensource.org/licenses/GPL-3.0/) 

# PyWish

This application will help you manage your wishes and create collections of things you want!

## Functions

* You can create a wish-list;
* You can manage wish-list items;

### Use Case

#### Wish List

* The user can create a wish-list;
* The user can list all created wish-lists;
* The user can filter searches by name and description;
* The user can update wish-list names and descriptions;
* The user can turn on or off the wish-list;
* The user cannot create two or more wish-lists with the same name;
* The user cannot update the wish-list to share a name with another list;

#### Wish List Item

* The user can create items within wish-lists;
* The user cannot create more than one item with the same name and code;
* The user can list all items from one wish-list;
* The user can filter searches by wish-list, name, description and active status;
* The user can activate and deactivate items;
* The user can update item code (external code), name and description;

## How to start with docker-compose

To run the project follow these step:

``` yml
docker-compose down && docker-compose up -d
```

Next, create all migrations and apply them.

``` yml
docker exec pywishapp python3 pywishproject/manage.py makemigrations

docker exec pywishapp python3 pywishproject/manage.py migrate
```

Finally, you can access this url:

```text
    http://localhost:8992
```

## How to start with Docker

In order to run local with database, you can up the PostgreSQL container with this command:

```yml
docker run --name pywish-postgresql -p 5031:5432 -e POSTGRES_DB=pywishdb -e POSTGRES_USER=pywishuser -e POSTGRES_PASSWORD=pywishpostgres -d postgres
```

Next, you start env of `pip`, creating new env if one does not exist:

```bash
virtualenv venv
```

Now, you can add all requirements to your env:

```python
pip3 install -r requirements.txt
```

If using Windows, execute this to start the env:

```bash
source venv/Scripts/activate
```

If you use Linux or MacOS, execute this:

```bash
source venv/bin/activate
```

Next, create all migrations and apply them.

```python
python pywishproject/manage.py makemigrations

python pywishproject/manage.py migrate

python manage.py createsuperuser --username=admin --email=admin@pywishproject.com

```

### Author

* [Felipe Brum](https://github.com/fbrump/)

### Mantainers

* [Felipe Brum](https://github.com/fbrump/)

### Stack

* Python 3
* Django
* PostgreSQL
* NginX
* unittest
* Docker
* docker-compose

#### Licence

GPL 3.0
