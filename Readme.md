
To run the project we just following the steps:

```
docker-compose down && docker-compose up -d
```

Next, create all migrations and apply they.

```
docker exec pywishapp python3 pywishproject/manage.py makemigrations
docker exec pywishapp python3 pywishproject/manage.py migrate
```


