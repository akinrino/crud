from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.urls import reverse
#from django.contrib.auth import autenticate, login,logout

# Create your views here.
def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form' : form})   
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

'''
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
	        return render(request, "auth/Login.html", context)
    else:
        return render(request, "auth/Login.html", context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

'''