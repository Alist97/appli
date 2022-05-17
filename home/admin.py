from django.contrib import admin
from .models import Project
from .models import Activity
from .models import SubActivity
from .models import Type
from .models import Unit
from .models import emsissions


admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(SubActivity)
admin.site.register(Type)
admin.site.register(Unit)
admin.site.register(emsissions)



# Register your models here.
