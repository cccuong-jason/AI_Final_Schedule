from django.urls import path 
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_instructor/', views.add_instructor, name='addinstructors'),
    path('instructor_list/', views.inst_list_view, name='editinstructors'),
    path('delete_instructor/<int:pk>/', views.delete_instructor, name='deleteinstructors'),
    path('add_room/', views.add_room, name='addrooms'),
]