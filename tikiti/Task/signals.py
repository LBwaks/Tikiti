from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task, TaskHistory
from django.conf import settings


@receiver(pre_save, sender=Task)
def create_task_history(sender, instance, **kwargs):
    if not instance.pk:
        # New task, no history yet
        return

    # Get the old instance from DB
    old_task = Task.objects.get(pk=instance.pk)

    status_changed = old_task.status != instance.status
    assignee_changed = old_task.assigned_to != instance.assigned_to

    if status_changed or assignee_changed:
        TaskHistory.objects.create(
            task=instance,
            previous_status=old_task.status,
            current_status=instance.status,
            previous_assignee=old_task.assigned_to,  # or .__str__()
            current_assignee=instance.assigned_to
        )
        # Task.objects.update(updated_by=self.request.user)
        assignee_email = 'victorobwaku@gmail.com' #getattr(instance.assigned_to, 'email', None)
        if assignee_email:
            send_mail(
                subject=f"New Task Assigned: {instance.title}",
                message=f"You've been assigned to task: {instance.title}.\n\nDescription: {instance.description}",
                # from_email=settings.DEFAULT_FROM_EMAIL,
                from_email="obwakuvictor@gmail.com",
                recipient_list=[assignee_email],
                fail_silently=False
            )

@receiver(post_save, sender=Task)
def create_ticket(sender, instance, created, **kwargs):
    if created and not instance.ticket:
        sector = instance.sector.sector_name.upper()[:5]
        instance.ticket = f"{sector}-{instance.id}"
        Task.objects.filter(pk=instance.pk).update(ticket=instance.ticket)

@receiver(post_save, sender=Task)
def notify_assignee_on_assignment(sender, instance, created, **kwargs):
    if not created:
        return  # only notify on create for now

    assignee_email = getattr(instance.assigned_to, 'email', None)
    if assignee_email:
        send_mail(
            subject=f"New Task Assigned: {instance.title}",
            message=f"You've been assigned to task: {instance.title}.\n\nDescription: {instance.description}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[assignee_email],
            fail_silently=True
        )
