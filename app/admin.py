from django.contrib import admin

from .models import Courses, Teachers, Students

admin.site.register([Courses, Teachers, Students])
