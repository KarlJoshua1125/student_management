from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('attendance/', views.attendance, name='attendance'),
    path('update_student/', views.update_student, name='update_student'),
    path('deletestudent/<int:id>', views.deletestudent, name = 'deletestudent'),
]