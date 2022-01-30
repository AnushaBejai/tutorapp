from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import * 
from django.db.models import Q 
from django.core.paginator import Paginator
from .filters import tutorpostfilter
import pdb

# Create your views here.
def home(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        students=Students.objects.filter(tutor__name=request.user.username)
        context={
            'students':students,
        }
        
        return render(request,'tutor.html', context) 
    


    else:
        tutorpost=TutorPost.objects.all()
       
       
        filtered_posts=tutorpostfilter(request.GET, 
        tutorpost
        )
        context={
            'tutorpost':tutorpost,  'filtered_posts':filtered_posts, 
        }
        paginated_filtered_posts=Paginator(filtered_posts.qs, 4)
        page_number=request.GET.get('page')
        post_page_obj=paginated_filtered_posts.get_page(page_number)
        context['post_page_obj']=post_page_obj

        
        return render(request,'student.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=name,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
       return render(request,'login.html')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=UserCreationForm()
        if request.method=='POST':
            Form=UserCreationForm(request.POST)

            if Form.is_valid():
                currUser=Form.save()
                Tutor.objects.create(user=currUser,name=currUser.username)
                return redirect('login')
        context={
            'form':Form
        }
        return render(request,'register.html',context)


def applyPage(request):
    form=ApplyForm()
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'apply.html',context) 

def tutorpost(request):
    form= TutorpostForm 
    if request.method=='POST':
        form= TutorpostForm(request.POST)
        if form.is_valid():
            form.save()
            TutorPost.objects.create(tutor=request.user)
            

    context={'form':form}
    return render(request, 'tutorpost.html', context) 



def mypost(request):
    if  request.user.is_authenticated and not request.user.is_superuser:
        post=TutorPost.objects.filter(tutor__name=request.user.username)
        context={
                'myposts':post,
            }
        
        return render(request,'myposts.html', context)

def delete_tutorpost(request, post_id):
    if  request.user.is_authenticated and not request.user.is_superuser:
        selectedtutorpost=TutorPost.objects.get(id=post_id)
        selectedtutorpost.delete()
        return redirect('mypost')

        

def studentrequirement(request):
    form= StudentPostForm
    if request.method=='POST':
        form= StudentPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'studentposts.html', context) 
    

def requirements(request):
    requirement=studentpost.objects.all()
    context={
            'requirement':requirement,
        }
        
    return render(request,'requirements.html', context)