from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Task
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class TaskForm(forms.ModelForm):
    files = forms.FileField(required=False, widget=forms.ClearableFileInput(
            attrs={"required": False, "class": "form-control images", "multiple": False}
        ),)
    # description = forms.CharField(widget=CKEditorWidget(attrs={"class":"form-control description","required":"True"}))

    class Meta:
        model = Task
        fields = ("sector", "source", "issue_type", "customer_id", "title", "description",
                 "support_type", "priority", "start_date", "end_date", "assigned_to")
        widgets ={
            "sector": forms.Select(attrs={"class": "form-control sector", "required": "True"}),
            "start_date": forms.DateTimeInput(attrs={"class":"control-select start_date","type":"datetime-local"}),
            "end_date": forms.DateTimeInput(attrs={"class":"control-select start_date","type":"datetime-local"}),
            }
        # widgets={"description"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.required_css_class = 'required'
    
    def clean(self):
        cleaned_data = super().clean()
        customer_id = cleaned_data.get("customer_id")
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if isinstance(customer_id, str) and 0 < len(customer_id) < 5:
            raise ValidationError(_("Customer Id must be greater than 10 Characters"), code="invalid_customer_id")
        
        if isinstance(title, str) and 0 < len(title) < 10:
            raise ValidationError(_("Title must be greater than 10 Characters"), code="invalid_customer_id")
        
        if isinstance(description, str) and 0 < len(description) < 20:
            raise ValidationError(_("Description must be greater than 20 Characters"), code="invalid_customer_id")
            
    def clean_image(self):
        files = self.cleaned_data.get("files", False)
        if files:
            if files.size > 1*1024*1024:
                raise ValidationError(
                    _("File should be less than 5mbs"), code="invalid"
                )

        return files

        

class UpdateTaskForm(forms.ModelForm):
    files = forms.FileField(required=False, widget=forms.ClearableFileInput(
            attrs={"required": False, "class": "form-control images", "multiple": False}
        ),)
    class Meta:
        model = Task
        fields = ("sector", "source", "issue_type", "customer_id", "title", "description",
                 "support_type", "priority", "start_date", "end_date", "assigned_to")
        
        widgets = {
            "sector": forms.Select(attrs={"class": "form-control sector", "required": "True"}),
            "start_date": forms.DateTimeInput(attrs={"class":"control-select start_date","type":"datetime-local"}),
            "end_date": forms.DateTimeInput(attrs={"class":"control-select start_date","type":"datetime-local"}),
            }

    def clean(self):
        cleaned_data = super().clean()
        customer_id = cleaned_data.get("customer_id")
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if isinstance(customer_id, str) and 0 < len(customer_id) < 5:
            raise ValidationError(_("Customer Id must be greater than 10 Characters"), code="invalid_customer_id")
        
        if isinstance(title, str) and 0 < len(title) < 10:
            raise ValidationError(_("Title must be greater than 10 Characters"), code="invalid_customer_id")
        
        if isinstance(description, str) and 0 < len(description) < 20:
            raise ValidationError(_("Description must be greater than 20 Characters"), code="invalid_customer_id")
        
    def clean_image(self):
        files = self.cleaned_data.get("files", False)
        if files:
            if files.size > 1*1024*1024:
                raise ValidationError(
                    _("File should be less than 5mbs"), code="invalid"
                )

        return files
        

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