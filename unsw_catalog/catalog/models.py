from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    career = models.CharField(max_length=15)
    gened = models.BooleanField()
    description_markup = models.TextField()
    uoc = models.PositiveSmallIntegerField()
    faculty = models.CharField(max_length=60)
    school = models.CharField(max_length=60)
    campus = models.CharField(max_length=25)
    eftsl = models.DecimalField(max_digits=6, decimal_places=5)