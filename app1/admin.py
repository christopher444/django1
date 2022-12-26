from django.contrib import admin
from . models import TableA
class ChrisAdmin(admin.ModelAdmin):
  list_display = [field.name for field in TableA._meta.get_fields()]
admin.site.register(TableA,ChrisAdmin) 
# Register your models here.
