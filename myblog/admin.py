from django.contrib import admin
from models import *
# Register your models here


@admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','category','createdTime','editTime']

# admin.site.register(BlogContent,BlogContentAdmin)


@admin.register(Mesage)
class MesageAdmin(admin.ModelAdmin):
    list_display = ['id','leave_msg','createdTime','editTime']

# admin.site.register(Mesage,MesageAdmin)
