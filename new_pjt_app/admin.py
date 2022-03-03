from django.contrib import admin

# Register your models here.
from new_pjt_app import *
from new_pjt_app.models import first_model,skill_table

admin.site.register(first_model)
admin.site.register(skill_table)