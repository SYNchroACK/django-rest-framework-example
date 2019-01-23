# Step 04 - Settings

## Add configuration parameters

Open the file `api/settings.py` and add the following lines block after the line `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`:

```
...

#######################################################
# ---- Production Mode Configuration Parameters ----- #
#######################################################

# --- HTTP Strict Transport Security
# SECURE_HSTS_SECONDS = 3600
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# --- Header 'x-content-type-options: nosniff'
# SECURE_CONTENT_TYPE_NOSNIFF = True

# --- Header 'x-xss-protection: 1; mode=block'
# SECURE_BROWSER_XSS_FILTER = True

# --- SSL-only
# SECURE_SSL_REDIRECT = True

# --- Cookie Security
# SESSION_COOKIE_SECURE = True

# --- CSRF Security
# CSRF_COOKIE_SECURE = True

# --- Frame Security
# X_FRAME_OPTIONS = 'DENY'

# --- Pre Load List
# SECURE_HSTS_PRELOAD = True

# --- CORS
CORS_ORIGIN_ALLOW_ALL = True  # FIXME: change me in production mode
# CORS_ORIGIN_WHITELIST = (
#     '<SERVER-IP>',
# )

...
```

* **Note:** check the link https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/ to learn more about production settings.


## Install CORS support

```
pip3 install django-cors-headers
```

## Add `corsheaders` app to app list

Open the file `api/settings.py` and change the following lines block:

```
...

INSTALLED_APPS = [

    ...

    'corsheaders',
]

...
```

## Add `corsheaders` middleware to middlewares list

Open the file `api/settings.py` and change the following lines block:

```
...

MIDDLEWARE = [

    ...

    'corsheaders.middleware.CorsMiddleware',
]

...
```