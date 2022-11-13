from django.contrib import admin
from formatter.models import *

# Register your models here.
class Bank_result_Admin(admin.ModelAdmin):
    list_display = ['result']
    list_filter = ['result']
    search_fields = ['result']

admin.site.register(Bank_result, Bank_result_Admin)