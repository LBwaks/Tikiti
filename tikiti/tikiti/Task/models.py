from django.db import models
from tikiti.users.models import User
import uuid
from django.utils.translation import gettext_lazy as _
from django.urls import reverse,reverse_lazy
from tikiti.Profile.models import Assignees
# Create your models here.

# sector


class Sector(models.Model):
    sector_name = models.CharField(max_length=60, unique=True)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='user_sector', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    is_featured = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sector'

    def __str__(self):
        return self.sector_name


# source 

class Source(models.Model):
    source_name = models.CharField(max_length=60, unique=True)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Source'

    def __str__(self):
        return self.source_name


# support types

class Support(models.Model):
    support_type = models.CharField(max_length=60, unique=True)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Support'
        verbose_name_plural = 'Support'

    def __str__(self):
        return self.support_type
    
# status


class Status(models.Model):
    status = models.CharField(max_length=60, unique=True)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status
# issue


class Issue(models.Model):
    issue_type = models.CharField(max_length=60, unique=True)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'

    def __str__(self):
        return self.issue_type
# priority

   
class Priority(models.Model):
    priority_type = models.CharField(max_length=60, unique=True)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'

    def __str__(self):
        return self.priority_type

#

    
# task


class Task(models.Model):
    sector = models.ForeignKey(Sector, related_name='task_sector', verbose_name =_('Sector'), on_delete= models.CASCADE)    
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    source = models.ForeignKey(Source, related_name="task_source", verbose_name=_('Lead'),  on_delete=models.CASCADE)
    issue_type = models.ForeignKey(Issue, related_name="task_issue", verbose_name=_("Issue Type"), on_delete=models.CASCADE)
    customer_id = models.CharField(_('Customer No'), max_length=40)
    title = models.CharField(_('Title'), max_length=100)
    description = models.TextField(_('Description'))
    support_type = models.ForeignKey(Support, related_name="task_support_type", verbose_name=_('Support Type'), on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, related_name="task_status", verbose_name=_('Status'), on_delete=models.CASCADE,default=2)
    priority = models.ForeignKey(Priority, related_name="task_priority", verbose_name=_('Priority'), on_delete=models.CASCADE)
    start_date = models.DateTimeField(_("Start Date"), blank=True, null=True)
    end_date = models.DateTimeField(_("End Date"), blank=True, null=True)
    assigned_to = models.ForeignKey(Assignees, related_name='task_assignee', verbose_name=_('Assignee'), on_delete=models.CASCADE,default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created By')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_update_task', verbose_name='Update User', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('Task:task-details', kwargs={'slug': self.slug})

    

# task files

class TaskFiles(models.Model):
    task = models.ForeignKey(Task, related_name="task_files", on_delete=models.CASCADE)
    file = models.FileField(_('Attachments'), upload_to='tasks/attachement')    
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Task File'
        verbose_name_plural = 'Task Files'

    def __str__(self):
        return f"{self.task.title}-{self.id}"
    
# task history


class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    slug = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    previous_status = models.CharField(max_length=30)
    current_status = models.CharField(max_length=30)
    previous_assignee = models.CharField(max_length=30)
    current_assignee = models.CharField(max_length=30)    
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Task History'
        verbose_name_plural = 'Task History'

    def __str__(self):
        return f"{self.task.title}-{self.id}"
# task comments

#assigee

# class AssigneeHist(models.Model):
#     task=models.ForeignKey(Task,verbose_name='Assigned_task',on_delete=models.CASCADE)
#     assigned_by = models.ForeignKey(User,verbose_name='Assigned_by',related_name='assigned_by',on_delete=models.CASCADE)
#     assigned_to = models.ForeignKey(User,verbose_name='Assigned_to',related_name='assigned_tasks',on_delete=models.CASCADE)
#     comments=models.TextField(max_length=300)
#     assigned_date=models.DateTimeField(auto_now_add=True)
#     update_date = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name=' Assignee'
    
#     def __str__(self):
#         return f"{self.task.title} →"


# Task Comments

class  TaskComment(models.Model):
    task = models.ForeignKey(Task, verbose_name=_("Task"),related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name ='Task Comment'

        def __str__(self):
            return f"{self.task.title}"