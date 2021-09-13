from django import forms
from django.db import models

from .models import Student,Lecture


class StudentModel(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels ={
            'stu_rn':'Student_Roll_no',
            'stu_name':'Student_Name',
            'stu_marks':'Student_Marks'
        }
        

class LectureModel(forms.ModelForm):
    class Meta:
        model=Lecture
        fields='__all__'
        labels ={
            'lec_sal':'Lecturer_Salary',
            'lec_name':'Lecturer_Name'
        }
        widgets={
            'department':forms.CheckboxSelectMultiple()
        }