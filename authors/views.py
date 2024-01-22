from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post

# Create your views here.

def register(request):

    if request.method =='POST':
       form =forms.RegistrationFrom(request.POST)
       
       if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('register')
    else:
        form =forms.RegistrationFrom()
    return render(request,'Register.html',{'form':form,'type':'Registration'})



def user_login(request):
    if request.method == 'POST':
       form = AuthenticationForm(request=request,data=request.POST)
       if form.is_valid():
            name=form.cleaned_data['username']
            userPass=form.cleaned_data['password']
            user=authenticate(username=name,password=userPass)

            if user is not None:
                messages.success(request,'Logged Successfully')
                login(request,user)
                return redirect('home')
            else:
                return redirect('register')
    
    else:
        form = AuthenticationForm()
    return render(request,'Register.html',{'form':form,'type':'Login'})
              
    

@login_required(login_url='/login/')
def profile(request):
    post = Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'post':post})

@login_required(login_url='/login/')
def edit_profile(request):
    if request.method =='POST':
       form =forms.ChangeUserData(request.POST,instance=request.user)
       
       if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update Your Profile')
            return redirect('profile')
    else:
        form =forms.ChangeUserData(instance=request.user)
    return render(request,'edit_profile.html',{'form':form,})


@login_required(login_url='/login/')
def pass_change(request):
    if request.method =='POST':
       form =PasswordChangeForm(request.user, data=request.POST)
       
       if form.is_valid():
            form.save()
            messages.success(request,'Password Change Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form =PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})


def LogOut(request):
    logout(request)
    return redirect('register')