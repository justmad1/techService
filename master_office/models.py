from django.db import models

class Master(models.Model):
    name = models.CharField(max_length = 30, null = False)
    surname = models.CharField(max_length = 30, null = False)
    lastname = models.CharField(max_length = 30, null = False)
    gender = models.CharField(max_length = 10)
    rating = models.CharField(max_length = 20)
    description = models.TextField()

    def __str__(self):
        return self.name
