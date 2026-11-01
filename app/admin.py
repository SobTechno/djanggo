from django.contrib import admin

# Register your models here.
from django.db import models
from .models import User

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'required': False},
    }

admin.site.register(User, MyModelAdmin)
