from django.contrib import admin

from freelearning.models import Course
from freelearning.models import Lesson
from freelearning.models import Resource


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'public', 'user']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'public', 'course', 'user']


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'public', 'lesson', 'user']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Resource, ResourceAdmin)