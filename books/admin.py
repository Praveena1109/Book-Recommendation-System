from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class ViewAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(Favourite)
# admin.site.register(ReadList)
