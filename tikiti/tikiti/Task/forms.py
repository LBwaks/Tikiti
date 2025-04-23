from django import forms
# from ckeditor.widgets import CKEditorWidget
from .models import Task


class TaskForm(forms.ModelForm):
    files = forms.FileField(required=False, widget=forms.ClearableFileInput(
            attrs={"required": False, "class": "form-control images", "multiple": False}
        ),)
    class Meta:
        model = Task
        fields = ("sector", "source", "issue_type", "customer_id", "title", "description",
                 "support_type", "priority", "start_date", "end_date", "assigned_to")
        widgets ={"sector": forms.Select(attrs={"class": "form-control sector", "required": "True"})}
        

class UpdateTaskForm(forms.ModelForm):
    files = forms.FileField(required=False, widget=forms.ClearableFileInput(
            attrs={"required": False, "class": "form-control images", "multiple": False}
        ),)
    class Meta:
        model = Task
        fields = ("sector", "source", "issue_type", "customer_id", "title", "description",
                 "support_type", "priority", "start_date", "end_date", "assigned_to")
        widgets ={"sector": forms.Select(attrs={"class": "form-control sector", "required": "True"})}
        

class UpdateTaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("status",)
        widgets ={"status": forms.Select(attrs={"class": "form-control sector", "required": "True"})}


class UpdateTaskAssigneeForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("assigned_to",)
        widgets ={"assigned_to": forms.Select(attrs={"class": "form-control sector", "required": "True"})}