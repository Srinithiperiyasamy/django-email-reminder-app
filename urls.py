from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('add/', views.add_reminder, name='add_reminder'),
    path('edit/<int:id>/', views.edit_reminder, name='edit_reminder'),
     path('delete/<int:id>/', views.delete_reminder, name='delete_reminder'),
     path('test-email/', views.test_email),

 ]

