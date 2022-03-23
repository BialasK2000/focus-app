from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.BetaLoginView.as_view(), name='login'),
    path('logout/', views.BetaLogoutView.as_view(), name='logout'),
    path('', views.MainTasksView.as_view(), name='main-tasks'),
    path('focus-details/<int:pk>/', views.DetailTaskView.as_view(), name='detail-tasks'),
    path('focus-create/', views.CreateTaskView.as_view(), name='create-tasks'),
    path('focus-update/<int:pk>/', views.TaskUpdateView.as_view(), name='update-tasks'),
    path('focus-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete-tasks'),
]
