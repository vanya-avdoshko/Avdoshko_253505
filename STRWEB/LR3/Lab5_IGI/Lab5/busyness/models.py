from django.db import models
from core.models import Customer, User




class Employee(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, default="employee with suppliers")
    phone = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='employee_photos/', default= 'images/no.jpeg', verbose_name="Load a photo of product")
    is_employee = models.BooleanField('is_employee', default=False)
    email = models.EmailField(default='maks.kree@mail.ru')


    def __str__(self):
        return f"{self.user.username}"
    
class Supplier(models.Model):    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    res_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):    
    name = models.CharField(max_length=255)
 #   suppliers_id = models.ManyToManyField(Supplier, related_name="categories")
    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='images/', default= 'images/no.jpeg', verbose_name="Load a photo of product" )
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_id = models.OneToOneField(Article, on_delete=models.CASCADE)
    supplier = models.ManyToManyField(Supplier, related_name= "products") 
    
    def __str__(self) -> str:
        return self.name
    
    
class News(models.Model):
    title = models.CharField(max_length=255)
    first_part = models.TextField(max_length=50)
    text = models.TextField(max_length= 12500)
    image = models.ImageField(upload_to='images/', default= 'images/no.jpeg', verbose_name="Load a photo of product" )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'News {self.id}'
    
    
class Order(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return f'Order {self.id} from {self.supplier.name}'
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in order {self.order.id}'
    
class FAQ(models.Model):
   # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    products = models.ManyToManyField('Product', through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=25500)
    image = models.ImageField(upload_to='images/', default= 'images/no.jpeg')

    
    
    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
    
    
class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField()  # Процент скидки, например, 10 для 10%
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class UsedPromoCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    used_at = models.DateTimeField(auto_now_add=True)


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    promo_code = models.ForeignKey(PromoCode, null=True, blank=True, on_delete=models.SET_NULL)
    is_paid = models.BooleanField(default=False)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()


class Company(models.Model):
    about = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='logo/', default='images/no.jpeg')
    video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="Company Video")  # Поле для загрузки видео
    history_by_years = models.TextField(blank=True, verbose_name="History by Years")  # Поле для истории компании по годам
    requisites = models.TextField(blank=True, verbose_name="Company Requisites")  # Поле для реквизитов компании
    certificate = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Company Certificate")  # Поле для загрузки сертификатов

    def __str__(self):
        return f'Company {self.id}'
    
class Partner(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/', default='images/no.jpeg')
    website = models.URLField(max_length=200, blank=True, null=True)  # Добавлено поле для сайта

    def __str__(self):
        return self.name


class SliderSettings(models.Model):
    auto = models.BooleanField(default=False)
    delay = models.PositiveIntegerField(default=5)
    loop = models.BooleanField(default=False)
    navs = models.BooleanField(default=True)
    pags = models.BooleanField(default=True)
    stopMouseHover = models.BooleanField(default=False)

    def __str__(self):
        return f"Slider Settings (Auto: {self.auto}, Delay: {self.delay}, Loop: {self.loop})"



