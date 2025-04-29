from django.shortcuts import render
from tikiti.Task.models import Task, Status, Priority
from django.views.generic import ListView, TemplateView
from .forms import TaskSearchForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.


class HomeTemplateVIew(TemplateView):
    template_name = 'pages/home.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statuses"] = Status.objects.all()
        context['priorities'] = Priority.objects.all()
        return context
    



class TaskSearchView(ListView):
    model = Task
    template_name = 'pages/search.html'
    # context_object_name = 'results'
    # form_class = TaskSearchForm

    def get_queryset(self):
        queryset = super().get_queryset().select_related('sector', 'source', 
                                                         'issue_type','assigned_to')
        self.form = TaskSearchForm(self.request.GET or None)
    
        if self.form.is_valid():
            title = self.form.cleaned_data.get('title')
            # priority = self.form.cleaned_data.get("priority")
            priority = self.request.GET.get('priority',None)
            # status = self.form.cleaned_data.get("status")
            status = self.request.GET.get("status",None)

            if title:
                queryset = queryset.filter(title__icontains=title)

            if priority: # and priority != '0' and priority != '999999':
                try:                    
                    priority = get_object_or_404(Priority, pk=priority)
                    queryset = queryset.filter(Q(priority__priority_type__icontains=priority.priority_type))
                except ValueError:
                    pass

            if status:
                try:
                    status = get_object_or_404(Status, pk=status)
                    queryset = queryset.filter(Q(status__status__icontains=status.status))
                except ValueError:
                    pass
        
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
    
    
