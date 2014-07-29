from django.core.management.base import BaseCommand, CommandError
from catalog.models import Class, Course

class Command(BaseCommand):
    help = ('A temporary command for trying out code that is otherwise'
            'inconvenient to repeat with the shell.')

    def handle(self, *args, **options):
        course = Course(
            **{
                'campus': u'Sydney',
                'career': u'Undergraduate',
                'code': u'BIOM9028',
                'description_markup': u'<div>Fundamentals of producing a medical image, image collection techniques, image reconstruction algorithms. Detailed examination of the four main areas of medical imaging: Nuclear Medicine and Positron Emission Tomography, Diagnostic Radiology, Magnetic Resonance and image analysis methods. Clinical application of each area.</div>',
                'eftsl': u'0.12500',
                'faculty': u'Faculty of Engineering',
                'gened': u'N',
                'name': u'Medical Imaging',
                'school': u'Graduate School of Biomedical Engineering',
                'uoc': u'6'
            }
        )
        self.stdout.write(course.id)
        klass = Class(class_nbr=12123, activity='Lecture', course=course)
        klass.save()
        self.stdout.write('Course has id: %d' % course.id)