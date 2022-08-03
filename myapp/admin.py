from django.contrib import admin

from myapp.models import GetInfo
from myapp.models import PhotoFor
from myapp.models import AddProject
from myapp.models import AddInformation
from myapp.models import AddInformation1
from myapp.models import ProjectCategory


admin.site.register(GetInfo)
admin.site.register(PhotoFor)
admin.site.register(AddProject)
admin.site.register(AddInformation)
admin.site.register(ProjectCategory)
admin.site.register(AddInformation1)
