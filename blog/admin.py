from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Blogpost

class StudentResource(resources.ModelResource):
   class Meta:
      model = Blogpost
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

admin.site.register(Blogpost,StudentAdmin)
