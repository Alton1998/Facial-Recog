from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Attendanceapp.models import StartAttendance
def loginpage(request):
    return render(request,'loginpage.html',{})
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/loginpage/')
def login(request):
    if request.method=="POST":
        username=request.POST["Username"]
        password=request.POST["Password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/main/')
        else:
            stats="User Not Found"
            return render(request, 'loginpage.html', {"stats":stats})
@login_required(login_url='/loginpage/')
def main(request):
    return render(request,"main.html",{'a':'Start Attendance','action':'/attendance/'})
@login_required(login_url='/loginpage/')
def attendance(request):
    if request.method=="POST":
        u=StartAttendance.objects.create()
        u.Update='1'
        u.save()
        return render(request, "main.html", {'a':'Stop Attendance','action':'/stop/'})
def stop(request):
    if request.method=="POST":
        u=StartAttendance.objects.create()
        u.Update='0'
        u.save()
        return render(request, "main.html", {'a': 'Start Attendance', 'action': '/attendance/'})
@login_required(login_url='/loginpage/')
def students(request):
    return render(request,'students.html',{})
@login_required(login_url='/loginpage/')
def submit(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES.getlist('file')
        firstname=request.POST['FirstName']
        middlename=request.POST['MiddleName']
        lastname=request.POST['LastName']
        dirname=str.upper(firstname)+"-"+str(middlename)+"-"+str(lastname)
        path='images/'+dirname
        fs = FileSystemStorage(location=path)
        for f in myfile:
            fs.save(f.name,f)
        return HttpResponseRedirect("/students/")
    else:
        stats="We were unable to save your chosen files"
        return render(request, 'students.html', {'stats':stats})

