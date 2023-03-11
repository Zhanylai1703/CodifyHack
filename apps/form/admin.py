from django.contrib import admin
from .models import Form, FormHistory
# Register your models here.

admin.site.register(Form)
admin.site.register(FormHistory)