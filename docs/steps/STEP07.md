# Step 07 - FreeLearning App

## FreeLearning App Overview

The app `FreeLearning` will provide the following structure:

* **Course**
    - name: String(50)
    - description: String(500)
    - public: Boolean()
    - created: DateTime(now)
    - User: ForeignKey()

* **Lesson**
    - name: String(50)
    - description: String(500)
    - public: Boolean()
    - Course: ForeignKey()
    - User: ForeignKey()

* **Resource**
    - name: String("50")
    - description: String("500")
    - type: Enum("pdf", "youtube", "vimeo", "gdrive", "generic")
    - link: URL("500")
    - public: Boolean()
    - Lesson: ForeignKey()
    - User: ForeignKey()

## Create FreeLearning app

```
cd api/
python3 manage.py startapp freelearning
```

## Add `freelearning` app to app list

Open the file `api/settings.py` and change the following lines block:

```
...

INSTALLED_APPS = [

    ...

    'freelearning',
]

...
```

## Development

Please check the commit in order to find the code associated to:
* `freelearning/models.py`
* `freelearning/serializers.py`
* `freelearning/views.py`
* `freelearning/admin.py`

## Add `freelearning` URL paths

Open the file `api/urls.py` and add the following lines replacing the line `# Router URL Paths will be placed here later ...`:

```
...

from freelearning.views import CourseViewSet
from freelearning.views import LessonViewSet
from freelearning.views import ResourceViewSet

router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('resources', ResourceViewSet)

...
```