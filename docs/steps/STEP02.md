# Step 02 - Initialize Django REST Framework

## Install Django REST Framework

```
pip3 install djangorestframework
```

## Add `rest_framework` app to app list

Open the file `api/settings.py` and change the following lines block:

```
...

INSTALLED_APPS = [

    ...

    'rest_framework',
]

...
```

## Add `REST_FRAMEWORK` configuration

Open the file `api/settings.py` and add the following lines block in the end of the file:

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
    ],
}
```

## Add `LOGIN` and `LOGOUT` URL paths

Open the file `api/urls.py` and add the following line:

```
...

from django.urls import include

urlpatterns = [
    path('', include('rest_framework.urls')),

    ...
]

...
```

## Add `DefaultRouter` paths

Open the file `api/urls.py` and add the following lines block in the end of the file:

```
...

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Router URL Paths will be placed here later ...

urlpatterns += router.urls
```