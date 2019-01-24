# Step 09 - FreeLearning Filters

## Custom Filters

Current API allows all users and non-authenticated viewers to view any private (`public: false`) course, lesson or resource due the lack of filters.

Please check the commit in order to find the code associated to:
* `freelearning/filters.py`

## Apply custom permissions

Open the file `freelearning/views.py` and add the following lines:

```
...

from freelearning.filters import IsOwnerOrPublicFilterBackend

...

class CourseViewSet(ModelViewSet):

    ...

    filter_backends = (IsOwnerOrPublicFilterBackend,)

...

class LessonViewSet(ModelViewSet):

    ...

    filter_backends = (IsOwnerOrPublicFilterBackend,)

...

class ResourceViewSet(ModelViewSet):

    ...

    filter_backends = (IsOwnerOrPublicFilterBackend,)

...
```