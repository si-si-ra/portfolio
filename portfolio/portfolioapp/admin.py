from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Resume)
admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(ContactInfo)

