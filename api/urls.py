from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users/', views.UsersViewset, basename='user')

urlpatterns = [
    path('todos/', views.todosView),
    path('todos/<int:pk>/', views.todoDetailView), # Function based view:- todoDetailView
    path('users/', views.Users.as_view()), # Class based view Users 'GET', 'POST'
    path('users/<int:pk>/', views.UserDetail.as_view()), # Class based view:- Users 'PUT', 'DELETE'
    # path('users/',  views.UsersViewset.as_view()), # Class based view Users 'GET', 'POST

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view())
]