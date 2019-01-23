# Step 03 - API Documentation

## Install CoreAPI

```
pip3 install coreapi pygments markdown
```

## Add `docs` URL paths

Open the file `api/urls.py` and add the following lines:

```
...

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='API')),

    ...
]

...
```