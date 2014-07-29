from django.db import models

class Course(models.Model):
    code = models.CharField(
        verbose_name = 'Course Code', 
        max_length = 10
    )
    name = models.CharField(
        verbose_name = 'Course Name', 
        max_length = 60
    )
    career = models.CharField(
        verbose_name = 'Study Level/Career', 
        max_length = 15, 
        choices = map(lambda x: (x, x), ('Undergraduate', 'Postgraduate', 'Research'))
    )
    year = models.PositiveSmallIntegerField()
    faculty = models.CharField(max_length=60)
    school = models.CharField(max_length=100)
    campus = models.CharField(max_length=30)
    gened = models.BooleanField(
        verbose_name = 'General Education', 
        default = False
    )
    description_markup = models.TextField(verbose_name='Description (markup)')
    uoc = models.PositiveSmallIntegerField(
        verbose_name = 'Units of Credit', 
        default = 0
    )
    eftsl = models.DecimalField(
        verbose_name = 'Equivalent Full-time Student Load', 
        max_digits = 6,
        decimal_places = 5
    )
    url = models.URLField(max_length=80)
    
    class Meta:
        unique_together = ('code', 'career', 'year')

    #TODO: normalize description

# risky class definition here... seems to work though :/
class Class(models.Model):
    course = models.ForeignKey(Course)
    class_nbr = models.PositiveIntegerField()
    activity = models.CharField(max_length=25)