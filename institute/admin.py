from django.contrib import admin
from .models import Institute, School, Department, Programme, Course


admin.site.register(Institute)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Programme)
admin.site.register(Course)