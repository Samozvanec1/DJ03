from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=100)
    Like = models.CharField(max_length=2)
    spoiler = models.TextField() #text

    def __str__(self):
        return self.name

