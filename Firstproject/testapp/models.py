from django.db import models
from django.db.models.deletion import CASCADE


class Department(models.Model):
    dep_name=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.dep_name


class Student(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    stu_rn=models.IntegerField()
    stu_name=models.CharField(max_length=20)
    stu_marks=models.FloatField()

    def __str__(self):
        return self.stu_name

class Lecture(models.Model):
    department=models.ManyToManyField(Department)
    lec_sal=models.FloatField()
    lec_name=models.CharField(max_length=20)

    def written_by(self):
        return ",".join([str(p) for p in self.department.all()])

    def __str__(self):
        return self.lec_name
