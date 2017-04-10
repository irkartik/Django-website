from django.db import models

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.SlugField(max_length=100)

    def __str__(self):
        return self.catagory_name

class Post(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title