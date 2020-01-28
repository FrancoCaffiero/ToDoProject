from django.contrib import admin

from .models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    fields = ['id', 'title', 'description', 'state', 'created_date']


admin.site.register(ToDo, ToDoAdmin)
