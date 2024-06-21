from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Lead)
@admin.register(models.Lead)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company_name', 'contact_number', 'category', 'created_at')
    search_fields = ('full_name', 'email', 'company_name', 'contact_number')
    list_filter = ('category', 'created_at', 'updated_at') 