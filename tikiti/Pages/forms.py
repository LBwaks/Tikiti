from django import forms
from tikiti.Task.models import Task, Status, Priority
from django.utils.translation import gettext as _


class TaskSearchForm(forms.Form):
    title = forms.CharField(required=False, label="Title", widget=forms.TextInput(attrs={"class":"form-control title-search"})),
    priority = forms.ModelChoiceField(required=False, label="Priority", queryset=Priority.objects.all(), empty_label=_("None"),
                                      widget=forms.Select(attrs={"class":"form-control"}))
    status = forms.ModelChoiceField(required=False, label="Status", queryset=Status.objects.all(), empty_label="None",
                                    widget=forms.Select(attrs={"class":"form-control"}))