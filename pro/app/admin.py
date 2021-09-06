from django.contrib import admin
from . models import Jobs
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Jobs, AuthorAdmin)