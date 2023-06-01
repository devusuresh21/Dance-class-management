
from asyncio import Event, _register_task
from pyexpat.errors import messages
from selectors import EVENT_READ, EVENT_WRITE
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from platformdirs import user_data_dir

from Dancestudio import settings
from .models import Sign_up,user_login
from .models import events
from django import forms
from .models import events
from django.shortcuts import render, redirect


from .models import *
from django.contrib.auth import login,logout, authenticate
from datetime import date
from django.db.models import Max


# Create your views here.

def index(request):
    videos = Video.objects.all()
    return render(request, 'index.html', {'videos': videos})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sign_up

def user_login(request):
 
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        user = Sign_up.objects.filter(email=email, password=pwd)
        
        if user:
            request.session["u_id"] = user[0].id
            return redirect("user_home")
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'user_login.html')

def user_home(request):
    user_id = request.session.get("u_id")
    
    if not user_id:
        return redirect("user_login")
    
    user = Sign_up.objects.get(id=user_id)
    context = {
        "user": user
    }
    
    return render(request, 'user_home.html', context)






from django.db.models import Max
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign_up

def sign_up(request):
    error = ""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
      
        
        new_sign_up = Sign_up.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            contact_no=contact_no,
            email=email,
            password=password,
      
            regDate=date.today()
         )
        new_sign_up.save()
       
        
        

        return render(request, 'index.html')
    else:
        return render(request, 'sign_up.html', {'regno': Sign_up.objects.count() + 1001})

from django.shortcuts import render, redirect
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register
def register_user(request):
    id = request.session.get("u_id")
    if not id:
        return redirect('login')  # Redirect if the user is not logged in

    sign_up = Sign_up.objects.get(id=id)
    dance = Category.objects.all()  # Retrieve all available dance types

    if request.method == 'POST':
        selected_dance_types = request.POST.getlist('dancetype')
        age = request.POST.get('age')

        try:
            userreg = Register(userreg=sign_up, Age=age)
            userreg.save()  # Save the Register instance first

            # Set the many-to-many relationship using the "dancetypes" attribute
            for dance_type_id in selected_dance_types:
                dance_type = Category.objects.get(id=dance_type_id)
                userreg.dance.add(dance_type)

            messages.success(request, 'Registration successful!')
            return redirect('user_home')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('register')

    return render(request, 'register.html', {'data': sign_up, 'dance': dance})



    
from .models import events

def event_list(request):
    id = request.session.get("u_id")
    user=Sign_up.objects.get(id=id)
    events_data = events.objects.all()
    c=confirmed_events.objects.filter(user=user)
    context = {'events': events_data,'confirmed':c}
    return render(request, 'events.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import events

def events_list(request):
    events = events.objects.all()
    return render(request, 'events.html', {'events': events})

def confirm_event(request,pk):
    id = request.session.get("u_id")
    user=Sign_up.objects.get(id=id)
    ev=events.objects.get(id=pk)
    new=confirmed_events.objects.create(user=user,event=ev)
    new.save()
    return redirect("http://127.0.0.1:8000/events/")














def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['old']
        n = request.POST['new']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changepassword.html', locals())

    
from django.shortcuts import render
from .models import Video

def video(request):
    videos = Video.objects.all()
    return render(request, 'video.html', {'videos': videos})


def category(request):
    ct=Register.objects.all()
    return render(request,"category.html",{"ct":ct})

def usercategories(request):
    cat = Category.objects.all()
    return render(request,"categories.html",{"cat":cat})

def stream(request):
    id=request.GET.get(id)
    video=Register.objects.filter(userreg=id)
    return render(request,'register.html',{"video":video})


from django.shortcuts import render
from .models import Sign_up
def my_Profile(request):
    id = request.session.get("u_id")
    sign_up = Sign_up.objects.get(id=id)
    register = Register.objects.filter(userreg=sign_up).first()
    registered_dance_types = []
    age = None  # Initialize age variable

    if register:
        registered_dance_types = register.dance.all().values_list('name', flat=True)
        age = register.Age  # Retrieve the value of the Age field

    return render(request, 'my_Profile.html', {'data': sign_up, 'register': register, 'registered_dance_types': registered_dance_types, 'age': age})

from django.shortcuts import render, redirect
from .models import Sign_up, Register

def edit_profile(request):
    id = request.session.get("u_id")
    sign_up = Sign_up.objects.get(id=id)
    
    success_message = ''

    if request.method == "POST":
        sign_up.first_name = request.POST.get('firstName')
        sign_up.last_name = request.POST.get('lastName')
        sign_up.gender = request.POST.get('gender')
        sign_up.contact_no = request.POST.get('contactNo')
        sign_up.email = request.POST.get('email')
        
        sign_up.save()

       

        success_message = 'Profile updated successfully.'
        # Redirect to My Profile page after saving the changes
        return render(request, 'edit_profile.html', {'sign_up': sign_up, 'success_message': success_message})

    return render(request, 'edit_profile.html', {'sign_up': sign_up, 'success_message': success_message})











def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('changepassword.html')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['old']
        n = request.POST['new']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changepassword.html', locals())


def viewdetails(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    dancedata = sign_up.objects.get(id=pid)
    totalcost = int(dancedata.duration) * int(dancedata.events.fees)
    

    return render(request, 'viewdetails.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')