from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def Userregister(request):
    form=RegisterForm()
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='Register.html'
    context={'form':form}
    return render(request,template_name,context)

def Userlogin(request):
    if request.method == 'POST':
        u= request.POST.get('uname')
        p= request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('student')

        else:
            messages.error(request,'Invalid cridential')
    template_name='Login.html'
    return render(request,template_name)

def Userlogout(request):
    logout(request)
    return redirect('register')

