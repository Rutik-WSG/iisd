from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(blog)
admin.site.register(Userlogin)
admin.site.register(BookMark)
admin.site.register(Comment)
admin.site.register(CategoryType)