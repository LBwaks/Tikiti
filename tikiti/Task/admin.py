from django.contrib import admin
from tikiti.Task.models import Sector, Source, Support, Status, Issue, Priority, Task, TaskMaterial,TaskHistory, TaskFiles,TaskComment#,Assignee
# Register your models here.


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):    
    list_display = ('sector_name', 'description')
    readonly_fields = ('slug', 'user')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
        return super().save_model(request, obj, form, change)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_name', 'description')
    readonly_fields = ('slug', 'user')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
        return super().save_model(request, obj, form, change)



@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('support_type', 'description')
    readonly_fields = ('slug', 'user')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
        return super().save_model(request, obj, form, change)



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'description')
    readonly_fields = ('slug', 'user')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
        return super().save_model(request, obj, form, change)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_type', 'description')
    readonly_fields = ('slug', 'user')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
        return super().save_model(request, obj, form, change)



@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('priority_type', 'description')
    readonly_fields = ('slug', 'user')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
        return super().save_model(request, obj, form, change)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('ticket','sector', 'slug', 'source','issue_type',
                    'customer_id','title', 'support_type',
                   'status' ,'priority','start_date','end_date',
                   'assigned_to')
    # readonly_fields = ('slug', 'user')
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.user_id:
    #         obj.user = request.user
    #         obj.save()
    #     return super().save_model(request, obj, form, change)


@admin.register(TaskFiles)
class TaskFilesAdmin(admin.ModelAdmin):
    list_display = ('task', 'file')
    readonly_fields = ('task',)
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.user_id:
    #         obj.user = request.user
    #         obj.save()
    #     return super().save_model(request, obj, form, change)



@admin.register(TaskHistory)
class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ('task', 'previous_status','current_status', 
                    'previous_assignee', 'current_assignee')
    readonly_fields = ('slug', 'task')
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.user_id:
    #         obj.user = request.user
    #         obj.save()
    #     return super().save_model(request, obj, form, change)

# @admin.register(Assignee)
# class AssigneeAdmin(admin.ModelAdmin):
#     list_display=['task','assigned_date']

@admin.register(TaskComment)
class TaskComments(admin.ModelAdmin):
    list_display=('task','user','comment','create_date')
    readonly_fields =('user',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user=request.user
            obj.save()
        return super().save_model(request, obj, form, change)

# @admin.register(TaskHistory)
# class TaskHIstory(admin.ModelAdmin):
#     list_display = ('task', 'previous_status', 'current_status', 'previous_assignee', 'current_assignee','create_date', 'update_date')
#     readonly_fields = ('task', 'previous_status', 'current_status', 'previous_assignee', 'current_assignee','create_date', 'update_date')

# @admin.register(TaskMaterial)
# class TaskMAterial(admin.ModelAdmin):
#     list_display ='all'

admin.site.register(TaskMaterial)