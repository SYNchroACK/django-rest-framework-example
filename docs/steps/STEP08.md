# Step 08 - FreeLearning Permissions

## Custom Permissions

Current API allows all users to change any course, lesson or resource from other users due the lack of permissions.

Please check the commit in order to find the code associated to:
* `freelearning/permissions.py`

## Apply custom permissions

Open the file `freelearning/views.py` and add the following lines:

```
...

# from rest_framework.permissions import IsAuthenticated
from freelearning.permissions import IsOwnerOrReadOnlyPublicPermission

...

class CourseViewSet(ModelViewSet):

    ...

    permission_classes = (IsOwnerOrReadOnlyPublicPermission,)

...

class LessonViewSet(ModelViewSet):

    ...

    permission_classes = (IsOwnerOrReadOnlyPublicPermission,)

...

class ResourceViewSet(ModelViewSet):

    ...

    permission_classes = (IsOwnerOrReadOnlyPublicPermission,)

...
```