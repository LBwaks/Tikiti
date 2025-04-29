from django.urls import path
from .views import TaskSearchView,HomeTemplateVIew

app_name = 'Pages'

urlpatterns = [
    path('', HomeTemplateVIew.as_view(), name='home'),
    path('search/', TaskSearchView.as_view(), name="search"),
]