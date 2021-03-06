from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.BetaLoginView.as_view(), name='login'),
    path('logout/', views.BetaLogoutView.as_view(), name='logout'),
    path('register/', views.BetaRegisterView.as_view(), name='register'),
    path('', views.MainTasksView.as_view(), name='main-tasks'),
    path('profile/', views.profile, name='users-profile'),
    path('completed-tasks/', views.DeletedTasksView.as_view(), name='completed-tasks'),
    path('focus-details/<int:pk>/', views.DetailTaskView.as_view(), name='detail-tasks'),
    path('focus-create/', views.CreateTaskView.as_view(), name='create-tasks'),
    path('focus-update/<int:pk>/', views.TaskUpdateView.as_view(), name='update-tasks'),
    path('focus-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete-tasks'),
    path('focus-confirm/<int:pk>/', views.TaskInvisibleView.as_view(), name='confirm-tasks'),
]
