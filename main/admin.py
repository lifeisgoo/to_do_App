from django.contrib import admin
from .models import CategoryModel, TasksModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']



@admin.register(TasksModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'created_at']

