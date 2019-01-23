# Step 05 - Authentication

## Add `rest_framework.authtoken` app to app list

Open the file `api/settings.py` and change the following lines block:

```
...

INSTALLED_APPS = [

    ...

    'rest_framework.authtoken',
]

...
```

## Change `REST_FRAMEWORK` configuration

Open the file `api/settings.py` and add the following line:

```
...

REST_FRAMEWORK = {

    ...

    'DEFAULT_AUTHENTICATION_CLASSES': [
        
        ...
        
        'rest_framework.authentication.TokenAuthentication',
    ],

    ...

}

...
```


## Install Djoser

```
pip3 install djoser
```

## Add `djoser` app to app list

Open the file `api/settings.py` and change the following lines block:

```
...

INSTALLED_APPS = [

    ...

    'djoser',
]

...
```

## Add `DJOSER` configuration

Open the file `api/settings.py` and add the following lines block in the end of the file:

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = '<USERNAME>@gmail.com'
# EMAIL_HOST_PASSWORD = '<PASSWORD>'

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/account/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'SERIALIZERS': { },
    'EMAIL': {
        'activation': 'djoser.email.ActivationEmail',
        'confirmation': 'djoser.email.ConfirmationEmail',
        'password_reset': 'djoser.email.PasswordResetEmail',
    },
}
```

## Add `djoser` URL paths

Open the file `api/urls.py` and add the following line:

```
...

urlpatterns = [

    ...

    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken')),

    ...
]

...
```

## Install JWT

```
pip3 install djangorestframework-jwt djangorestframework_simplejwt
```

## Change `REST_FRAMEWORK` configuration

Open the file `api/settings.py` and add the following line:

```
...

REST_FRAMEWORK = {

    ...

    'DEFAULT_AUTHENTICATION_CLASSES': [
        
        ...
        
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],

    ...

}

...
```

## Add `JWT` configuration

Open the file `api/settings.py` and add the following lines block in the end of the file:

```
import datetime

JWT_AUTH = {
#   'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
#   'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
#   'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
#   'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
#   'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
#   'JWT_SECRET_KEY': settings.SECRET_KEY,
#   'JWT_GET_USER_SECRET_KEY': None,
#   'JWT_PUBLIC_KEY': None,
#   'JWT_PRIVATE_KEY': None,
#   'JWT_ALGORITHM': 'HS256',
#   'JWT_VERIFY': True,
#   'JWT_VERIFY_EXPIRATION': True,
#   'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#   'JWT_AUDIENCE': None,
#   'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': True,
#   'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#   'JWT_AUTH_HEADER_PREFIX': 'JWT',
#   'JWT_AUTH_COOKIE': None,
}
```

## Add `JWT` URL paths

Open the file `api/urls.py` and add the following line:

```
...

from django.urls import include

urlpatterns = [
    ...

    path('auth/', include('djoser.urls.jwt')),

    ...
]

...
```