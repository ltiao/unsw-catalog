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
        help_text = 'Available for General Education',
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
    prereqs = models.ManyToManyField('self', verbose_name='Prerequisites', symmetrical=False)
    exclusions = models.ManyToManyField('self', symmetrical=True)
    accessed = models.DateTimeField(
        verbose_name = 'Last Accessed',
        help_text = 'Last time the source was accessed by crawler', 
        auto_now = True
    )
    url = models.URLField(max_length=80)
    
    class Meta:
        unique_together = ('code', 'career', 'year')

    def __unicode__(self):
        return u'{code} - {name}'.format(code=self.code, name=self.name)

    #TODO: normalize description

class Class(models.Model):
    course = models.ForeignKey(Course, related_name='classes')
    class_nbr = models.PositiveIntegerField(unique=True)
    activity = models.CharField(max_length=25)
    section = models.CharField(max_length=5)
    teaching = models.CharField(verbose_name='Teaching Period', max_length=50)
    status = models.CharField(max_length=10)
    enrolments = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    offering_start = models.DateField()
    offering_end = models.DateField()
    census_date = models.DateField()
    mode = models.CharField(verbose_name='Instruction Mode', max_length=30)
    consent = models.CharField(max_length=30)
    accessed = models.DateTimeField(
        verbose_name = 'Last Accessed',
        help_text = 'Last time the source was accessed by crawler', 
        auto_now = True
    )
    updated = models.DateTimeField(
        verbose_name = 'Last Updated',
        help_text = 'Last time source itself was updated',
    )
    url = models.URLField(max_length=80)

    class Meta:
        verbose_name_plural = 'classes'

    def __unicode__(self):
        return u'{course_name} - {activity} ({class_nbr})'.format(course_name=self.course.name, 
            activity=self.activity, class_nbr=self.class_nbr)

class Meeting(models.Model):
    # need to add a French twist to the field name
    classe = models.ForeignKey(Class, verbose_name='Class', related_name='meetings')
    day = models.CharField(max_length=5)
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    location = models.CharField(max_length=100)
    weeks = models.CharField(max_length=20)
    instructor = models.CharField(max_length=50)