from django.db import models

class Thesis(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    abstract = models.TextField()

    def __str__(self):
        return self.title
