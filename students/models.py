from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name
