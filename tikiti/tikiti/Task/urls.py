from django.urls import path
from .views import Test

app_name = 'Task'

urlpatterns = [
    path("", view=Test, name='test')
]




