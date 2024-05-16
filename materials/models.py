# materials/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to='materials/files/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
