from django.urls import path 
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('timetable_generation/', views.timetable, name='timetable'),
    #Instructor
    path('add_instructor/', views.add_instructor, name='addinstructors'),
    path('delete_instructor/<int:pk>/', views.delete_instructor, name='deleteinstructors'),
    path('add_instructor/<int:pk>/update_instructor', views.update_instructor, name='updateinstructors'),
    #Room
    path('add_room/', views.add_room, name='addrooms'),
    path('delete_room/<int:pk>/', views.delete_room, name='deleterooms'),
    path('add_room/<int:pk>/update_room/', views.update_room, name='updaterooms'),
    #Subject
    path('add_subject/', views.add_subject, name='addsubjects'),
    path('delete_subject/<int:pk>/', views.delete_subject, name='deletesubjects'),
    path('add_subject/<int:pk>/update_subject/', views.update_subject, name='updatesubjects'),
    #Shift
    path('add_shift/', views.add_shift, name='addshifts'),
    path('delete_shift/<int:pk>/', views.delete_shift, name='deleteshifts'),
    path('add_shift/<int:pk>/update_shift/', views.update_shift, name='updateshifts'),
    #Department
    path('add_department/', views.add_department, name='adddepartments'),
    path('delete_department/<int:pk>/', views.delete_department, name='deletedepartments'),
    path('add_department/<int:pk>/update_department/', views.update_department, name='updatedepartments'),
    #Section
    path('add_section/', views.add_section, name='addsections'),
    path('delete_section/<str:pk>/', views.delete_section, name='deletesections'),
    path('add_section/<str:pk>/update_section/', views.update_section, name='updatesections'),
    path('test/',views.test,name='tests')
    ]