from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from storeapp.models import Contact, FormSubmission

from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        submission = Contact(name=name, email=email, message=message)
        submission.save()

        return redirect('/contact/')

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def userpage(request):
    return render(request, 'userpage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('storeapp:userpage')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('storeapp:signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('storeapp:signup')

        user = User.objects.create_user(username=username, password=password)
        return redirect('storeapp:login')
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




def form(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provide = ', '.join(request.POST.getlist('materials'))


        submission = FormSubmission.objects.create(
            username=username,
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department=department,
            course=course,
            purpose=purpose,
            materials=materials_provide
        )

        order_confirmed = "Order Confirmed"

        return render(request, 'form.html', {'order_confirmed': order_confirmed})

    return render(request, 'form.html')









