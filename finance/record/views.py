from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Expenditure
from django.db.models import Sum


def home(request):
    return render(request,'home.html')

@login_required(login_url='/')
def add_finance(request):
    if request.method == "POST":
        purpose = request.POST['purpose']
        amount = request.POST['amount']
        exp = Expenditure(purpose=purpose,amount=amount, username = request.user)
        exp.save()
    return redirect(dashboard)

@login_required(login_url='/')
def dashboard(request):
    datas = Expenditure.objects.filter(username = request.user)
    
    total = datas.aggregate(Sum('amount'))
    params = {'datas':datas,'total':total['amount__sum']}
    return render(request,'dashboard.html',params)

@login_required(login_url='/')
def delete(request):
    if request.method == 'POST':
        hidden = request.POST['hidden']
        delete_item = Expenditure.objects.get(id=hidden)
        delete_item.delete()

        print(hidden)

   
    return redirect(dashboard)



def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f"You have successfully registered as {username} ")
            form = RegisterUser()
            redirect(home)
            
    else:
        form = RegisterUser()
    params = {'form': form, 'title': 'SignUp'}
    return render(request, 'register.html', params)


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:

            messages.error(
                request, 'Username and Password didnot match. Try again ')
    return redirect(dashboard)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')