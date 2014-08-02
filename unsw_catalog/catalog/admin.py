from django.contrib import admin
from catalog.models import Course, Class, Meeting

class ClassInline(admin.TabularInline):
    model = Class
    extra = 5

class CourseAdmin(admin.ModelAdmin):
	inlines = [ClassInline]
	list_display = ('code', 'name', 'career', 'year')
	list_filter = ('career', 'faculty', 'school', 'campus', )
	search_fields = ['name', 'description_markup']
	ordering = ('code',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Class)
admin.site.register(Meeting)
