from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class MyUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    profile_image = forms.ImageField(required = False)

    class Meta:
        model = User
        fields = ['username', 'email',  'phone_number', 'profile_image', 'password1', 'password2']

    def save(self, commit = True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user = user,
                phone_number = self.cleaned_data['phone_number'],
                profile_image = self.cleaned_data.get('profile_image')
            )
        return user