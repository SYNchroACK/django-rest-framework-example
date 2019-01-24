from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication

# from rest_framework.permissions import IsAuthenticated
from freelearning.permissions import IsOwnerOrReadOnlyPublicPermission

from freelearning.filters import IsOwnerOrPublicFilterBackend

from rest_framework.viewsets import ModelViewSet

from freelearning.serializers import CourseSerializer
from freelearning.serializers import LessonSerializer
from freelearning.serializers import ResourceSerializer

from freelearning.models import Course
from freelearning.models import Lesson
from freelearning.models import Resource


class CourseViewSet(ModelViewSet):
    
    allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JSONWebTokenAuthentication)   
    permission_classes = (IsOwnerOrReadOnlyPublicPermission,)
    filter_backends = (IsOwnerOrPublicFilterBackend,)

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonViewSet(ModelViewSet):

    allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsOwnerOrReadOnlyPublicPermission,)
    filter_backends = (IsOwnerOrPublicFilterBackend,)

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ResourceViewSet(ModelViewSet):

    allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsOwnerOrReadOnlyPublicPermission,)
    filter_backends = (IsOwnerOrPublicFilterBackend,)

    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()