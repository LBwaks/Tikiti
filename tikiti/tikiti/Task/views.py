from django.shortcuts import render
from tikiti.Task.models import Task, Sector, Source, Support, Status, Issue, Priority, TaskHistory, TaskFiles,TaskComment#,Assignee
from tikiti.Profile.models import Assignees
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, UpdateTaskForm, UpdateTaskStatusForm, UpdateTaskAssigneeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/tasks.html"
    login_url = ""
    context_object_name = 'tasks'
    paginate_by = 2 

    def get_queryset(self):
        queryset = Task.objects.select_related().defer()
        return queryset
    # more info
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_sectors"] = Sector.objects.annotate(sector_count=Count('task_sector')).prefetch_related("task_sector")
        context['task_prioritys'] = Priority.objects.annotate(priority_count=Count("task_priority")).prefetch_related("task_priority")
        context['task_statuses'] = Status.objects.annotate(status_count=Count("task_status")).prefetch_related("task_status")
        context['task_issues'] = Issue.objects.annotate(issue_count=Count("task_issue")).prefetch_related("task_issue")
        context['task_assigness'] = Assignees.objects.annotate(assignee_count=Count("task_assignee")).prefetch_related("task_assignee")
        context['statuses'] = Status.objects.all()
        context['priorities'] = Priority.objects.all()
        return context
    

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task-details.html'
    context_object_name = "task"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #task = self.get_object()
        context['status_form'] = UpdateTaskStatusForm(instance=self.object)
        context['assignee_form'] = UpdateTaskAssigneeForm(instance=self.object)
        return context


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create-task.html'
    success_message = "Task Created Successfully"
    success_url = "/"
    
    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = self.request.user        
        task.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            TaskFiles.objects.create(task=task, file=file)        
        return super(CreateTaskView, self).form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'task/update-task.html'
    success_message = "Task Edited Successfully"
    # success_url = "/"
    
    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            TaskFiles.objects.create(task=task, file=file)   
        # messages.success(self.request("Task Update Successfully"))     
        return super(UpdateTaskView, self).form_valid(form)
    
    # def form_invalid(self, form):
    #     messages.error(self.request("Task Update Unsuccessfull"))
    #     return super(UpdateTaskView, self).form_invalid(form)
        
    
    

class UpdateTaskStatusView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskStatusForm
    template_name = 'task/update-status.html'
    success_message = "Task Status Changed"
    #success_url = "/"
    

class UpdateTaskAssigneeView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskAssigneeForm
    template_name = 'task/update-assignee.html'
    success_message = "Task Assignee Changed"
    # success_url = "/"
    
   

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete-task.html'
    success_message = 'Task Deleted'
    success_url = '/'
    

@login_required
def Test(request):    
    context = {}
    return render(request, "task/test.html", context)

