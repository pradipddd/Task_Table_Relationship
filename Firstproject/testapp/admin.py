from django.contrib import admin
from .models import Department,Student,Lecture


class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','dep_name']
admin.site.register(Department,DepartmentAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','stu_rn','stu_name','stu_marks','department']
admin.site.register(Student,StudentAdmin)

class LectureAdmin(admin.ModelAdmin):
    list_display=['id','lec_sal','lec_name','written_by']
admin.site.register(Lecture,LectureAdmin)
