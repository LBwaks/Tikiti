from django.urls import path
from .views import TaskSearchView

app_name = 'Pages'

urlpatterns = [

    path('search/', TaskSearchView.as_view(), name="search"),

]