from django.shortcuts import render
from .models import ContactEntry
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User  # Import Django's built-in User model
from django.contrib.auth.views import PasswordResetView

from django.core.mail import send_mail



from django.shortcuts import render, redirect

from .models import UserProfile



# Create your views here.
def home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'About.html')

def Service(request):
    return render(request, 'Service.html')
def Contact(request):
    return render(request, 'Contact.html')


    
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Check if email is provided
        if email:
            # Save form data to the database
            new_contact = ContactEntry.objects.create(
                name=name,
                phone=phone,
                email=email,
                subject=subject,
                message=message
            )

            # Send email notification to fixed recipient
            send_mail(
                subject,
                f'Name: {name}\nPhone: {phone}\nUser Email: {email}\nMessage: {message}',
                'your_email@example.com',  # Your email address
                ['hariharan23052001@gmail.com'],  # Fixed recipient email address
                fail_silently=False,
            )

           



            return JsonResponse({'message': 'Form submitted successfully!'})
        else:
            return JsonResponse({'message': 'Email is required!'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method!'}, status=400)

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_profile = UserProfile.objects.get(email=email)

            if user_profile.password == password:
                # If passwords match, create a user instance
                user, created = User.objects.get_or_create(username=email, email=email)
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL after successful login
            else:
                error_message = 'Invalid email or password'
        except UserProfile.DoesNotExist:
            error_message = 'User does not exist'

        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if UserProfile.objects.filter(email=email).exists():
            error_message = 'Email already exists. Please use a different email.'
            return render(request, 'login.html', {'error_message': error_message})
        
        try:
            # Create a UserProfile instance
            user_profile = UserProfile.objects.create(name=name, email=email, password=password)
            
            # Attempt to authenticate the user directly after signup
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL after successful login
            else:
                error_message = 'Failed to log in after signup. Please try logging in.'
                return render(request, 'login.html', {'error_message': error_message})
        except Exception as e:
            print(f"Error creating user profile: {e}")

    return render(request, 'login.html')
def check_email_existence(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if UserProfile.objects.filter(email=email).exists():
            # Email exists in the database
            return JsonResponse({'exists': True})
        else:
            # Email doesn't exist in the database
            return JsonResponse({'exists': False})

    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request'}, status=400)


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User


def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        # Check if the current password is valid
        if not user.check_password(current_password):
            messages.error(request, 'Invalid current password.')
            return redirect('change_password')

        # Check if the new password matches the confirmation
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('change_password')

        # Update the user's password
        user.set_password(new_password)
        user.save()

        # Update the session to prevent logout
        update_session_auth_hash(request, user)

        messages.success(request, 'Your password was successfully updated!')
        return redirect('profile')  # Redirect to the user's profile page

    return render(request, 'change_password.html')

