from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def add_post(request):
    if request.method =='POST':
       form =forms.Add_Post(request.POST)
       
       if form.is_valid():
            form.instance.author=request.user
            form.save()
            return redirect('home')
    else:
        form =forms.Add_Post()
    return render(request,'add_post.html',{'form':form})

@login_required(login_url='/login/')
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    form =forms.Add_Post(instance=post)
    if request.method =='POST':
       form =forms.Add_Post(request.POST,instance=post)
       
       if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'add_post.html',{'form':form})


@login_required(login_url='/login/')
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')