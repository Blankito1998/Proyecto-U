from django.shortcuts import render, redirect
from django.http import HttpResponse
from ventas.models import Producto
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm

# Create your views here.

 

def ver_productos(request):
    productos_list = Producto.objects.all()
    context = {'object_list': productos_list}
    return render(request,'listar_productos.html', context)

def ver_index(request):
    if request.user.is_authenticated:
        return render(request, "Index.html")
    return redirect('login')

def register(request):
    
    form = UserCreationForm()
    if request.method == "POST":
        
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():

            
            user = form.save()

             
            if user is not None:
                
                do_login(request, user)
                
                return redirect('Login.html')

    
    return render(request, "Registro.html", {'form': form})

def ver_contactenos(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ver_index')
    else:
        form = PostForm()
    return render(request, 'Contactenos.html',{'form': form})

def ver_mision(request):
    return render(request, 'Mision&Vision.html')

def ver_quienes(request):
    return render(request, 'QuienesSomos.html')

def login(request):
    
    form = AuthenticationForm()
    if request.method == "POST":
        
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            
            user = authenticate(username=username, password=password)

            
            if user is not None:
                
                do_login(request, user)
                
                return redirect('ver_index')

    
    return render(request, "Login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('ver_index')

def pass_reset(request):
    return render(request, 'reset_password.html')

def pass_reset2(request):
    return render(request, 'password_reset_done.html')

def pass_reset3(request):
    return render(request, 'password_reset_email.html')

def pass_reset4(request):
    return render(request, 'password_reset_confirm')

def pass_reset5(request):
    return render(request, 'password_reset_complete')

