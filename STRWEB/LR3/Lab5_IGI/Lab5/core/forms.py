import re
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from busyness.models import Employee, Category

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'phone', 'date_of_birth']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your phone number in format +375 (29) XXX-XX-XX',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'type': 'date',
        'placeholder': 'Your phone number in format +375 (29) XXX-XX-XX'
    }))

    def clean_number(self):
        phone = self.cleaned_data.get('phone')
        pattern = r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$'
        if not re.match(pattern, phone):
            raise ValidationError('Phone number must be in the format: +375 (29) XXX-XX-XX')
        return phone
    
    
class SignUpEmpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2', 'phone', 'date_of_birth', 'photo']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    position = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Position',
        'class': 'w-full py-4 px-6 rounded-xl'
    }), required=False)
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your phone number in format +375 (29) XXX-XX-XX',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'type': 'date',
        'placeholder': 'Date of birth'
    }))
    
    photo = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'class': 'form-control-file',
        'placeholder': 'Employees photo'
    }))
    
    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get('position')
        if not position:  # Если поле position не указано в форме
            cleaned_data['position'] = "employee with suppliers"  # Устанавливаем значение по умолчанию
        return cleaned_data
    
    
  
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'name', 'position', 'email', 'phone', 'photo']
