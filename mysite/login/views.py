from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user' : current_user}
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).count() > 0:
            return HttpResponse('Username already exists')
        else:
            user = User(username = username, password = password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')   
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = User.objects.filter(username = username, password = password)
        if check_user:
            request.session['user'] = username
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
