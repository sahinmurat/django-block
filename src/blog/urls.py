from django.urls import path
from .views import home, todo_create, todo_update, todo_delete,list

urlpatterns = [
   
  
    path('', home, name = 'home'),
]
