from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User   # Use get_user_model if using custom User model
from . models import Customer

from django.contrib import messages




# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer

def show_account(request):
    context = {}
    if request.method == 'POST':
        if 'register' in request.POST:
            context['register'] = True
            try:
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                address = request.POST['address']
                phone = request.POST['phone']

                # Create user account
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email           
                )

                # Create user Customer account
                customer = Customer.objects.create(
                    name=username,
                    user=user,
                    phone=phone,
                    address=address         
                )
                success_message = "User registered successfully"
                messages.success(request, success_message)
            except Exception as e:
                error_message = "Duplicate username or email is not allowed"
                messages.error(request, error_message)

        elif 'login' in request.POST:
            context['register'] = False
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_staff:  # Check if the user is a super admin
                    login(request, user)
                    messages.info(request, 'Welcome admin')
                    return redirect('shop_customerList')
                else:
                    login(request, user)
                    messages.info(request, 'Welcome')
                    return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Try again!')
                return render(request, 'account.html', context)

    return render(request, 'account.html', context)


def shop_customerList(request):
    docdb=Customer.objects.all()
    return render(request, 'shop_banner.html',{'doc':docdb})

