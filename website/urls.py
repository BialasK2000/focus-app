from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainTasksView.as_view(), name='main-tasks-view'),
    path('focus-details/<int:pk>/', views.DetailTaskView.as_view(), name='detail-tasks-view'),
]
