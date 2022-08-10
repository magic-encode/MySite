from django.contrib import admin

from myapp.models import GetInfo
from myapp.models import PhotoFor
from myapp.models import AddProject
from myapp.models import ProjectCategory


admin.site.register(GetInfo)
admin.site.register(PhotoFor)
admin.site.register(AddProject)
admin.site.register(ProjectCategory)

