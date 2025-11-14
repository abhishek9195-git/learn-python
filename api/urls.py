from django.urls import path
from . import views

# urlpatterns = [
#     path('todos/', views.Todo)

# ]
urlpatterns = [
    # ... other paths ...
    path('todos/', views.todosView),
    path('todos/<int:pk>/', views.todoDetailView), # Function based view:- todoDetailView
    path('users/', views.Users.as_view()), # Class based view Users 'GET', 'POST'
    path('users/<int:pk>/', views.UserDetail.as_view()) # Class based view:- Users 'PUT', 'DELETE'
]