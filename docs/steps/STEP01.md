# Step 01 - Initialize Django Project

## Install Django

```
pip3 install django
```

## Create Django Project `api`

```
cd django-rest-framework-example/
django-admin startproject api
```

## Create Migrations

```
cd api/
python3 manage.py migrate
```

## Create Admin Account

```
cd api/
python3 manage.py createsuperuser
> Username (leave blank to use 'root'): admin
> Email address: admin@example.com
> Password: ********
> Password (again): ********
> Superuser created successfully.
```