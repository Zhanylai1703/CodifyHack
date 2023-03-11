from django.contrib import admin
from django_mptt_admin.admin import MPTTModelAdmin
from .models import *

# Register your models here.

admin.site.register(Establishments)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(QA)