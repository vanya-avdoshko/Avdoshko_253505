from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from . import forms
from .services.catfact import fact_cat
from .services.dogs import dogs
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm,template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('tags/', views.tags, name='tags'),
    path('school/', views.school, name='school'),
    path('school2/', views.school2, name='school2'),
    path('weather/', views.weather, name='weather'),
    path('chart_data/', views.chart_data, name='chart_data'),
    path('glossary/', views.glossary, name='glossary'),
    path('terms/', views.terms, name='terms'),
    path('vacancy/', views.vacancy_list, name='vacancy'),
    re_path('contact/', views.employee_list, name='employee_list'),
    path('employees/', views.employees, name='employees'),
    #path('<int:pk>/', views.product_detail, name='product_detail'),
    re_path(r'^add_employee/$', views.add_employee, name='add_employee'),
    path('fact/', fact_cat, name='cat_facts'),
    path('dogs/', dogs, name='dogs'),
    path('partners/', views.partners, name='partners'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)