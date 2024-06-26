from django.shortcuts import render, redirect
from main.forms import CreateUserForm, LoginForms, AddRecordForm, UpdateRecordForm, ViewForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from main.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"main/index.html")

@login_required(login_url='login')
def dashbord(request):
    records = Record.objects.all()
    context = {'records':records}
    return render(request,"main/dashboard.html",context=context)

def login(request):
    form = LoginForms()
    if request.method == "POST":
        form = LoginForms(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/dashboard')
    context = {'form':form}
    return render(request,"main/login.html",context=context)

def logout(request): 
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("/login")

def register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('/login')
    context = {'form':form}
    return render(request, 'main/register.html',context=context)

@login_required(login_url='login')
def add_record(request):
    form = AddRecordForm
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record was created!")
            return redirect("/dashboard")
    context = {'form':form}
    return render(request,"main/add-record.html",context=context)

@login_required(login_url='login')
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record was updated!")
            return redirect("/dashboard")
    context = {'form':form}
    return render(request,"main/update-record.html",context=context)

@login_required(login_url='login')
def view_record(request,pk):
    record = Record.objects.get(id=pk)
    form = ViewForm(instance=record)
    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
    context = {'form':form,'id':record.id}
    return render(request, 'main/view-record.html',context=context)

@login_required(login_url='login')
def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record was deleted!")
    return redirect("/dashboard")