from django.shortcuts import render,redirect
from .models import Department, Student,Lecture
from .forms import StudentModel,LectureModel
from django.contrib import messages


def Student_register_view(request):
    form=StudentModel()
    if request.method=='POST':
        form=StudentModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    template_name='StudentRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def Lecturer_register_view(request):
    form=LectureModel()
    if request.method=='POST':
        form=LectureModel(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecture_list')
    template_name='LectureRegister.html'
    context={'form':form}
    return render(request,template_name,context)


def Student_list_view(request):
    stu=Student.objects.all()
    template_name='StudentShow.html'
    context={'stu':stu}
    return render(request,template_name,context)

def Lecturer_list_view(request):
    lec=Lecture.objects.all()
    template_name='LecturerShow.html'
    context={'lec':lec}
    for i in lec:
        print(i.department.all())
    return render(request,template_name,context)

def Student_update_view(request,stu_update):
    stu=Student.objects.get(id=stu_update)
    form=StudentModel(instance=stu)
    if request.method=='POST':
        form=StudentModel(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    template_name='StudentRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def Lecture_update_view(request,lec_update):
    lec=Lecture.objects.get(id=lec_update)
    form=LectureModel(instance=lec)
    if request.method=='POST':
        form=LectureModel(request.POST,instance=lec)
        if form.is_valid():
            form.save()
            return redirect('lecture_list')
    template_name='LectureRegister.html'
    context={'form':form}
    return render(request,template_name,context)


def Student_delete_view(request,stu_delete):
    stu_del=Student.objects.get(id=stu_delete)
    stu_del.delete()
    return redirect('student_list')

def Lecture_delete_view(request,lec_delete):
    lec_del=Lecture.objects.get(id=lec_delete)
    lec_del.delete()
    return redirect('lecture_list')


def Search_view(request):
    if request.method=='POST':
        search=request.POST.get('search')
        stu=Student.objects.filter(stu_name__contains=search)
        lec=Lecture.objects.filter(lec_name__contains=search)
        dep=Department.objects.filter(dep_name__contains=search).first()
        print(dep)
        if dep is not None:
            stu_dep=Student.objects.filter(department_id=dep)
            lec_dep=Lecture.objects.filter(department=dep.id)
            template_name='isearch.html'
            context={'stu_dep':stu_dep,'lec_dep':lec_dep,'dep':dep}
            return render(request,template_name,context)
        template_name='isearch.html'
        context={'stu':stu,'lec':lec}
        return render(request,template_name,context)
    template_name='isearch.html'
    context={'abc':'abc'}
    return render(request,template_name,context)



# def Searchview(request):
#     if request.method == 'POST':
#         radio=request.POST.get('dep')
#         if radio == 'Department':
#             search=request.POST.get('search')
#             dep_obj=Department.objects.get(dep_name=search)
#             dep_id=dep_obj.id
#             lecresult=Lecture.objects.filter(department=dep_id)
#             sturesult=Student.objects.filter(department_id=dep_id)
#             template_name='SearchDepartement.html'
#             context={'lecresult':lecresult,'sturesult':sturesult}
#             return render(request,template_name,context)
        
#         elif radio == 'Student':
#             search=request.POST.get('search')
#             sturesult=Student.objects.filter(stu_name=search)
#             template_name='SearchStudent.html'
#             context={'sturesult':sturesult}
#             return render(request,template_name,context)

#         elif radio == 'Lecturer':
#             search=request.POST.get('search')
#             lecresult=Lecture.objects.filter(lec_name=search)
#             template_name='SearchLecturer.html'
#             context={'lecresult':lecresult}
#             return render(request,template_name,context)
        

#     template_name='Search.html'
#     context={}
#     return render(request,template_name,context)



