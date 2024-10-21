from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from django.views import View

from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm

class LoginView(View):
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #clean_data เมื่อตรงกัย field ใน model
            user = form.get_user() 
            login(request,user)
            return redirect('blog-list')  

        return render(request,'login.html', {"form":form})


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')