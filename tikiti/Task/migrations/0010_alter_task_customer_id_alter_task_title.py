# Generated by Django 5.1.8 on 2025-05-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0009_task_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='customer_id',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Customer No'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Title'),
        ),
    ]
