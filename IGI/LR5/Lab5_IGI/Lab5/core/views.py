import calendar
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignupForm, SignUpEmpForm
from django.contrib.auth import login
from core.models import Customer, User
from busyness.models import Product, News, Employee, Category, Vacancy
from django.contrib.auth import authenticate, login as login_user, logout
from django.utils import timezone
from calendar import HTMLCalendar
from .utils import get_user_time 
import calendar
from datetime import datetime
import tzlocal
from django.contrib.auth.decorators import user_passes_test, login_required


@login_required
def index(request):
    sort_by = request.GET.get('sort_by')

    products = Product.objects.all()    
    news = News.objects.all()
    
    if sort_by == 'name':
        products = products.order_by('name')
    if sort_by == 'price':
        products = products.order_by('price')   
    if sort_by == 'category_id':
        products = products.order_by('category_id') 

    user_time_info = get_user_time()

    return render(request, 'core/index.html', {
        'products': products,
        'news': news,
        **user_time_info,
    })


def about(request):
    return render(request, 'core/about.html')  

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')

def calculate_age(birth_date: datetime):
    current_date = datetime.now().date()
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age

def is_not_admin(user):
    return user.is_authenticated and not user.is_superuser and not user.is_employee

def is_admin(user):
    return user.is_authenticated and user.is_superuser

def is_worker(user):
    return user.is_authenticated and (user.is_superuser or user.is_employee)

def is_customer(user):
    return user.is_authenticated and user.is_customer


import re

def signup(request):
    if request.method == 'POST':  # Проверяем, была ли отправлена форма
        form = SignupForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)  # Сохраняем нового пользователя в базу данных
            date_of_birth = form.cleaned_data.get('date_of_birth')
            user_age = calculate_age(date_of_birth)
            if user_age < 18:
                form.add_error('date_of_birth', 'Вам нет 18!')
                return render(request, 'core/signup.html', {'form': form, 'msg': 1})
            
            
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
           # return HttpResponse(phone)
            pattern = r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$'
            if not re.match(pattern, phone):
                form.add_error('phone', 'Phone number must be in the format: +375 (29) XXX-XX-XX')
                return render(request, 'core/signup.html', {'form': form})
            
            user.is_customer = True
            user.save() 
            Customer.objects.create(user=user, phone=phone, address=address)
            #logging.info(f"{user.username} зарегистрирован")         

       #     login(request, user)  # Аутентифицируем нового пользователя
            return redirect("/")  # Перенаправляем на главную страницу
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

def add_employee(request):
    form = SignUpEmpForm(request.POST, request.FILES)
    if form.is_valid():
        
        user = form.save(commit=False)  # Сохраняем нового пользователя в базу данных
        date_of_birth = form.cleaned_data.get('date_of_birth')
        user_age = calculate_age(date_of_birth)
        if user_age < 18:
            form.add_error('date_of_birth', 'Вам нет 18!')
            return render(request, 'core/add_employee.html', {'form': form, 'msg': 1})
        
        
        phone = form.cleaned_data['phone']
        name = form.cleaned_data['name']
        position = form.cleaned_data['position']
        photo = form.cleaned_data['photo']
        # return HttpResponse(phone)
        pattern = r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$'
        if not re.match(pattern, phone):
            form.add_error('phone', 'Phone number must be in the format: +375 (29) XXX-XX-XX')
            return render(request, 'core/add_employee.html', {'form': form})
        
        user.is_employee = True
        is_employee = True
        user.save()        
        Employee.objects.create(user=user, phone=phone, name=name, position=position, photo=photo, is_employee=is_employee)
        
        #logging.info(f"{user.username} зарегистрирован")         

    #     login(request, user)  # Аутентифицируем нового пользователя
        return redirect("/")  # Перенаправляем на главную страницу
    else:
        form = SignUpEmpForm()

    return render(request, 'core/add_employee.html', {'form': form})


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/vacancy.html', {'vacancies': vacancies})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/contact.html', {'employees': employees})


