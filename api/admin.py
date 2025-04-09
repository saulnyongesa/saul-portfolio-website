from django.contrib import admin
from api.models import User, Project, Email, Skill

# Register your models here.
admin.site.register([
    User,
    Project,
    Email,
    Skill,
])