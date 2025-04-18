from django.db import models
# from django.contrib.auth.models import User
from tikiti.users.models import User

# Create your models here.


class Assignees(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='assignee', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Assignee'
    
    def __str__(self):
        return f"{self.assignee.username}"