from rest_framework import serializers

from freelearning.models import Course
from freelearning.models import Lesson
from freelearning.models import Resource


class CourseSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('created',)


class LessonSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = '__all__'
    

class ResourceSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Resource
        fields = '__all__'