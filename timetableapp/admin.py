from django.contrib import admin

# Register your models here.
from .models import Course, Faculty, Student, Admin

admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Admin)
