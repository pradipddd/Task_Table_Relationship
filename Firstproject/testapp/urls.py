from django.urls import path
from .views import Student_register_view,Lecturer_register_view,Student_list_view,Lecturer_list_view,Student_update_view,Lecture_update_view,Student_delete_view,Lecture_delete_view,Search_view

urlpatterns=[
    path('student/',Student_register_view,name='student'),
    path('lecturer/',Lecturer_register_view,name='lecturer'),
    path('student_list/',Student_list_view,name='student_list'),
    path('lecture_list/',Lecturer_list_view,name='lecture_list'),
    path('student_update/<str:stu_update>',Student_update_view,name='student_update'),
    path('lecturer_update/<str:lec_update>',Lecture_update_view,name='lecturer_update'),
    path('student_delete/<str:stu_delete>',Student_delete_view,name='student_delete'),
    path('lecturer_delete/<str:lec_delete>',Lecture_delete_view,name='lecturer_delete'),
    path('search/',Search_view,name='search')
    
]