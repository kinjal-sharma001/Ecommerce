from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings

from .models import UserProfile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid() :
            user = form.save()
            login(request, user)

            send_mail(
                subject='Welcome to Our Store!',
                message='Thank you for signing up. We’re excited to have you onboard!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('home')
    else:
        form = MyUserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_profile_view(request):
    # user = UserProfile.objects.get(user = request.user)
    user, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/user_profile.html', {'user': user})