from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    public = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return "%s" % self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'course')

    def __str__(self):
        return "%s" % self.name


class Resource(models.Model):

    TYPES = (
        ('PDF', 'pdf'),
        ('Youtube Video', 'youtube'),
        ('Vimeo Video', 'vimeo'),
        ('Google Document', 'gdrive'),
        ('Generic', 'generic'),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=100, choices=TYPES)
    link = models.URLField(max_length=500)
    public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'lesson')

    def __str__(self):
        return "%s" % self.name