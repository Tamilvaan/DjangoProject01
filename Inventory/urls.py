from django.urls import path
from .views import *

urlpatterns =[
    path('student/add/',Student_add),
    path('student/list/',student_list),
    path('student/list/delete/<int:id>',delete,name="student_delete"),
    path('student/list/update/<int:id>',update,name="student_update"),
]