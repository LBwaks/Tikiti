from django.shortcuts import render,get_object_or_404,redirect
from tikiti.Task.models import Task, Sector, Source, Support, Status, Issue, Priority, TaskHistory, TaskFiles,TaskMaterial,TaskComment#,Assignee
from tikiti.Profile.models import Assignees
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, UpdateTaskForm, UpdateTaskStatusForm, UpdateTaskAssigneeForm,COmmentTaskForm,TaskMaterialForm,TaskMaterialEditForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
from django.utils.text import slugify
from django.http import Http404
from tikiti.users.models import User
# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/tasks.html"
    login_url = ""
    context_object_name = 'tasks'
    paginate_by = 20 

    def get_queryset(self):
        queryset = Task.objects.select_related().defer().order_by("-create_date")
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
        context['comments'] = self.object.comments.all().order_by('-create_date')
        context['comment_form'] = COmmentTaskForm()
        context['materials'] = TaskMaterial.objects.filter(task=self.object)
        return context
    
    def post(self,request,*args, **kwargs):
        task = self.get_object()
        form = COmmentTaskForm(request.POST)
        
        if form.is_valid():
            comment=form.save(commit=False)
            comment.task=task
            comment.user=request.user
            comment.save()
            return redirect(task.get_absolute_url())
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
        


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create-task.html'
    success_message = "Task Created Successfully"
    # success_url = "/"
    
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
    

# class TaskCommentsView(LoginRequiredMixin, CreateView):
#     model = TaskComment
#     success_message ="Comment Added"
#     form_class = COmmentTaskForm

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
    

class TaskSectorView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 20
    template_name = 'task/task-sector.html'

    def get_queryset(self):
        self.sector = get_object_or_404(Sector, slug=self.kwargs.get('slug'))
        return super().get_queryset().filter(sector=self.sector).select_related('sector', 'source', 
                                                        'issue_type', 'assigned_to').order_by("-create_date")    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sector"] = self.sector 
        return context

    
class TaskStatusView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task-status.html'
    paginate_by = 20

    def get_queryset(self):
        self.status = get_object_or_404(Status, slug=self.kwargs.get('slug'))
        return super().get_queryset().filter(status=self.status).select_related('sector', 'source', 
                                                        'issue_type', 'assigned_to').order_by("-create_date")  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = self.status
        return context
    
    

class TaskPriorityView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task-priority.html'
    paginate_by = 20

    def get_queryset(self):
        self.priority = get_object_or_404(Priority, slug=self.kwargs.get('slug'))
        return super().get_queryset().filter(priority=self.priority).select_related('sector', 'source', 
                                                        'issue_type', 'assigned_to').order_by("-create_date")  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["priority"] = self.priority
        return context
    
    

class TaskIssueView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task-issue.html'
    paginate_by = 20

    def get_queryset(self):
        self.issue_type = get_object_or_404(Issue, slug=self.kwargs.get('slug'))
        return super().get_queryset().filter(issue_type=self.issue_type).select_related('sector', 'source', 
                                                        'issue_type', 'assigned_to').order_by("-create_date") 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue_type"] = self.issue_type
        return context
    


class TaskAssigneeView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task-assignee.html'
    paginate_by = 20

    def get_queryset(self):
        self.assignee_to = get_object_or_404(Assignees, id=self.kwargs.get('pk'))
        return super().get_queryset().filter(assigned_to=self.assignee_to).select_related('sector', 'source', 
                                                        'issue_type', 'assigned_to').order_by("-create_date")  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assigned_to"] = self.assignee_to
        context['task_status_count'] = Task.objects.filter(assigned_to=self.assignee_to).select_related('task_assignee', 'task_status').values("assigned_to__assignee").annotate(count=Count('id'))
        return context
    
    

class MyTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/my-tasks.html'
    paginate_by = 20
    context_object_name = 'tasks'

    def get_assigned_user(self):
        username = slugify(self.kwargs.get("username", '').strip())
        try:
            user = User.objects.get(username=username)
            assigned_user = Assignees.objects.select_related("assignee").get(assignee=user)
            return assigned_user
        
        except User.DoesNotExist:
            raise Http404("User not found")

    def get_queryset(self):
        self.assigned_user = self.get_assigned_user()
        queryset = Task.objects.filter(assigned_to=self.assigned_user).select_related('assigned_to').order_by("-create_date")
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assigned_user"] = self.assigned_user
        context['task_status_count'] = Task.objects.filter(assigned_to=self.assigned_user).select_related('assigned_to').values("status__status").annotate(count=Count("id")).order_by("status")
        return context
    

class AddTaskMaterial(LoginRequiredMixin, CreateView):
    model = TaskMaterial
    form_class = TaskMaterialForm
    template_name = 'task/add-materials.html'

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, slug=self.kwargs.get('slug'))
        return super().dispatch(request, *args, **kwargs)
   
    def form_valid(self, form):

        material = form.save(commit=False)        
        material.task = self.task
        material.user = self.task.assigned_to
        material.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('Task:task-details', kwargs={'slug': self.task.slug})    
    
    
class EditTaskMaterial(LoginRequiredMixin, UpdateView):
    model = TaskMaterial
    form_class = TaskMaterialEditForm
    template_name = 'task/edit-materials.html'

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, slug=self.kwargs.get('slug'))
        return super().dispatch(request, *args, **kwargs)
   
    def form_valid(self, form):

        material = form.save(commit=False)        
        # material.task = self.task
        material.user = self.request.user
        material.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('Task:task-details', kwargs={'slug': self.task.slug})
    

@login_required
def Test(request):    
    context = {}
    return render(request, "task/test.html", context)

