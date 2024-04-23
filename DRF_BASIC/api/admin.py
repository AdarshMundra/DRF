from django.contrib import admin
from .models import Stundet
# Register your models here.


@admin.register(Stundet)
class StudenAdmin(admin.ModelAdmin):
    list_display = ['id','stuName','roll','city']

