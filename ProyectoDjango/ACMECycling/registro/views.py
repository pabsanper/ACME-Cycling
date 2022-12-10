from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index_view(request):
    return render(request,'index.html')
@login_required()

def dashboard_view(request):
    return render(request,'dashboard.html')
    
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')  
        else:
            messages.info(request, 'Datos erróneos de registro')  
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})