from django.urls import path
from . import views

urlpatterns = [
    path('add_todo/', views.AddTodo.as_view(), name='add_todo'),
]
