from django.urls import path
from .views import Test, TaskListView, TaskDetailView, CreateTaskView, MyTaskView, DeleteTaskView,TaskAssigneeView, TaskIssueView,TaskPriorityView, UpdateTaskView, TaskStatusView,UpdateTaskStatusView, UpdateTaskAssigneeView,TaskSectorView

app_name = 'Task'

urlpatterns = [
    path("", TaskListView.as_view(), name='tasks'),
    path("details/<slug>/", TaskDetailView.as_view(), name="task-details"),
    path("create", CreateTaskView.as_view(), name='create'),
    path("delete/<slug>/", DeleteTaskView.as_view(), name="delete"),
    path("edit/<slug>", UpdateTaskView.as_view(), name='edit'),
    path("change-status/<slug>", UpdateTaskStatusView.as_view(), name='change-status'),
    path("change-assignee/<slug>", UpdateTaskAssigneeView.as_view(), name='change-assignee'),
    path('sector/<slug>', TaskSectorView.as_view(), name='task-sector'),
    path('status/<slug>', TaskStatusView.as_view(), name='task-status'),
    path('priority/<slug>', TaskPriorityView.as_view(), name='task-priority'),
    path('issue/<slug>', TaskIssueView.as_view(), name='task-issue'),
    path('assignee/<pk>', TaskAssigneeView.as_view(), name='task-assignee'),
    path('my-task/<username>', MyTaskView.as_view(), name='my-task')
    
]




