from django.contrib import admin
from .models import Assignees

# Register your models here.

@admin.register(Assignees)
class AssigneeAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'assignee']
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.user_id:
    #         obj.user = request.user
    #         obj.save()
    #     return super().save_model(request, obj, form, change)
