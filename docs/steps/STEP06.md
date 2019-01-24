# Step 06 - Runserver #1

## Allowed Hosts

Open the file `api/settings.py` and change `ALLOWED_HOSTS` to the following line:

```
...

ALLOWED_HOSTS = ['*']  # FIXME: change me in production mode

...
```

## Migrate and Run

```
cd api/
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080
```

## Browsable API Page

Access the browsable API page.

* **URL:** http://127.0.0.1:8080/

## Admin Page

Access the admin page and provide the admin credentials.

* **URL:** http://127.0.0.1:8080/admin/

## Documentation Page

Access the documentation page.

* **URL:** http://127.0.0.1:8080/docs/