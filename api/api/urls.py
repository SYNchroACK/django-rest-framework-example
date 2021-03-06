"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='API')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from freelearning.views import CourseViewSet
from freelearning.views import LessonViewSet
from freelearning.views import ResourceViewSet

router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('resources', ResourceViewSet)

urlpatterns += router.urls