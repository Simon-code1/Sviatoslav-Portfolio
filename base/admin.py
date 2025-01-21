from django.contrib import admin
from .models import Project, Certification, Post, Skill
from .forms import ProjectAdminForm, PostAdminForm

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Certification)
admin.site.register(Skill)