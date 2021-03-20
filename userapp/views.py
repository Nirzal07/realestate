from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProfilePic, ProfilePicForm, UserRegisterationForm, Favourites, ProfileUpdateForm
from webapp.models import PropertyDetails, Comment

def register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        if password == confirm_password:
            User.objects.create_user(first_name=first_name, last_name=last_name, username= username, password=password)
            user= authenticate(username=username, password= password)
            login(request, user)
            return redirect('webapp:home')
        else:
            messages.error(request,"Passwords didn't match")
    context = {}
    return render(request, 'user_app/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return redirect('webapp:home')
        else:
            messages.error(request, 'Username or Password Incorrect')
            return redirect('userapp:user_login')
    else:
        return render(request, 'user_app/login.html')

def user_logout(request):
    logout(request)
    return redirect('webapp:home')

@login_required
def user_profile(request):
    favourites = Favourites.objects.filter(user= request.user)
    favourites_count= len(favourites)
    user_properties = PropertyDetails.objects.filter(seller= request.user)
    user_properties_count= len(user_properties)
    user_properties = user_properties[:3]
    #profile_picture = ProfilePic.objects.get(user= request.user)
        
    if request.method== 'POST':
        form= ProfileUpdateForm(request.POST)
        #form2= ProfilePicForm(request.POST, request.FILES)
        if form.is_valid: #and form2.is_valid:
            form.save()
            #n_form2= form2.save(commit=False)
            #n_form2.user = request.user
            #n_form2.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('userapp:profile')
    else:
        form= ProfileUpdateForm(instance= request.user)
        #form2= ProfilePicForm(instance=profile_picture)
    context= {
        'favourites': favourites,
        'properties': user_properties,
        #'profile_picture': profile_picture,
        'user_properties_count': user_properties_count,
        'favourites_count': favourites_count,
        'profile_update_form':form,
        #'profile_pic_update_form': form2
    }
    return render(request, 'user_app/profile_dashboard.html', context)