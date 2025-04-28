from django.shortcuts import render
from tikiti.Task.models import Task, Sector, Source, Support, Status, Issue, Priority, TaskHistory, TaskFiles,TaskComment#,Assignee
from django.views.generic import ListView
from .forms import TaskSearchForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.


class TaskSearchView(ListView):
    model = Task
    template_name = 'pages/search.html'
    context_object_name = 'results'
    # form_class = TaskSearchForm

    def get_queryset(self):
        queryset = super().get_queryset().select_related('task_sector', 'task_source', 
                                                         'task_issue','task_assignee')
        self.form = TaskSearchForm(self.request.GET or None)

        if self.form_valid():
            title = self.form.cleaned_data.get('title')
            priority = self.form.cleaned_data.get("priority")
            status= self.form.cleaned_data.get("status")

            if title:
                queryset = queryset.filter(title__icontains=title)

            if priority and priority != '0':
                priority = get_object_or_404(Priority, pk=priority)
                queryset = queryset.filter(Q(priority__name__icontains=priority.name))

            if status and status != '0':
                status = get_object_or_404(Status, pk=status)
                queryset = queryset.filter(Q(status__name_icontains=status.status))
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_id = self.request.GET.get('status', None)
        if status_id == '0':
            context['status'] = 'All Statuses'
        else:
            status = get_object_or_404(Status, pk=status_id)
            context['status'] = status.status

        context["search_form"] = self.form
        return context
    
    
