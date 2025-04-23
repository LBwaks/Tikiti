from django.urls import path
from .views import Test, TaskListView, TaskDetailView, CreateTaskView, DeleteTaskView, UpdateTaskView, UpdateTaskStatusView, UpdateTaskAssigneeView

app_name = 'Task'

urlpatterns = [
    path("", TaskListView.as_view(), name='tasks'),
    path("details/<slug>/", TaskDetailView.as_view(), name="task-details"),
    path("create", CreateTaskView.as_view(), name='create'),
    path("delete/<slug>/", DeleteTaskView.as_view(), name="delete"),
    path("edit/<slug>", UpdateTaskView.as_view(), name='edit'),
    path("change-status/<slug>", UpdateTaskStatusView.as_view(), name='change-status'),
    path("change-assignee/<slug>", UpdateTaskAssigneeView.as_view(), name='change-assignee'),
    
]




