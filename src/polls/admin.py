from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_id', 'amount']


admin.site.register(Category,CategoryAdmin)
