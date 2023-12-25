from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([
    Staff, StudentClasses, Subject, Student, Result, ReportCard
])
