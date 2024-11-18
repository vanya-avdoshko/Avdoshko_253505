from datetime import timezone
import statistics
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Cart, CartItem, Order, Product, Category, Article, News, PromoCode, Sale, SaleItem, Supplier, Employee, FAQ, OrderProduct, UsedPromoCode, Vacancy
from .forms import ProductForm, NewsForm, PromoCodeForm, ReviewForm, SupplierForm, OrderForm, OrderProductForm, FAQForm, ProductSearchForm
import logging
from core.models import Customer
import stripe
from django.conf import settings
from django.db.models import Avg, Sum, Count
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from django.contrib.auth.decorators import login_required
import statistics
from django.http import HttpResponseRedirect
import paypalrestsdk


from django.http import HttpResponse


logger = logging.getLogger(__name__)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            # Проверяем, что указана корректная категория
            if product.category and product.category.supplier == product.supplier:
                product.save()
                return redirect('/')
            else:
                # Если категория не соответствует поставщику, отобразить ошибку
                form.add_error('category', 'Invalid category for this supplier.')
    else:
        form = ProductForm()
    return render(request, 'busyness/add_product.html', {'form': form})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    form = ReviewForm() if request.user.is_authenticated and hasattr(request.user, 'customer') else None
    return render(request, 'busyness/product_detail.html', {
        'product': product,
        'form': form
    })
    
def new_detail(request, id):
    new = get_object_or_404(News, id=id)
    return render(request, 'busyness/new_detail.html' , {
        'new': new
    })

def delete_product(request, id):

    product = Product.objects.get(id=id)
    product.delete()    
    logger.info("Successfully deleted!")
    return redirect('/')

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            logger.info("Successfully edited!")

            return redirect('/')
    else:
        logger.error("Something wrong in your form!")

        form = ProductForm(instance=product)
    return render(request, 'busyness/edit_product.html', {'form': form})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)  # Добавляем request.FILES для загрузки файлов
        if form.is_valid():
            form.save()
            return redirect('/')  # Перенаправляем на страницу со списком новостей
    else:
        form = NewsForm()
    return render(request, 'busyness/add_news.html', {'form': form})



def delete_news(request, id):

    news = News.objects.get(id=id)
    news.delete()    
    return redirect('/')

def edit_news(request, id):
    news_item = get_object_or_404(News, id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('/')  # Перенаправляем на страницу со списком новостей
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'busyness/edit_news.html', {'form': form})

# views.py
def read_all_new(request, id):
    # Получаем объект новости или выводим 404 ошибку, если не найдено
    new = get_object_or_404(News, id=id)

    # Контекст данных, передаваемых в шаблон
    context = {
        'new': new
    }

    # Возвращаем HTML-шаблон с контекстом
    return render(request, 'busyness/read_all_new.html', context)

def news_list(request):
    news = News.objects.all()  
        
    return render(request, 'busyness/news_list.html', {'news': news})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('busyness:supplier_list')  # Перенаправляем на главную страницу после сохранения
    else:
        form = SupplierForm()
    return render(request, 'busyness/add_supplier.html', {'form': form})


def edit_supplier(request, id):   
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('busyness:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'busyness/edit_supplier.html', {'form': form})

def supplier_list(request):    
    suppliers = Supplier.objects.all()  
        
    return render(request, 'busyness/supplier_list.html', {'suppliers': suppliers})


def delete_supplier(request, id):
    if not request.user.is_superuser:
        return redirect('/') 
    supplier = Supplier.objects.get(id=id)
    supplier.delete()    
    return redirect('busyness:supplier_list')

def employees_suppliers(request):
    is_employee = True
    employee = Employee.objects.get(user=request.user)
    suppliers = Supplier.objects.filter(res_employee=employee)
    
    return render(request, 'busyness/suppliers.html', {'suppliers' : suppliers, 'is_employee' : is_employee})

def check_products(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    products = Product.objects.filter(supplier=supplier)
    
    return render(request, 'busyness/check_products.html', {'supplier': supplier, 'products': products})

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.total_price = 0
            order.save()

            for product_id, quantity in zip(request.POST.getlist('product'), request.POST.getlist('quantity')):
                product = Product.objects.get(id=product_id)
                quantity = int(quantity)
                
                OrderProduct.objects.create(order=order, product=product, quantity=quantity)
                
                product.stock += quantity
                product.save()
                
                order.total_price += product.price * quantity

            order.save()
            return redirect('busyness:order_success')  # Перенаправляем на страницу успеха заказа
    else:
        order_form = OrderForm()
        products = Product.objects.all()
        
        context = {
            'order_form': order_form,
            'products': products
        }
        return render(request, 'busyness/create_order.html', context)
    
def order_success(request):
    return render(request, 'busyness/order_success.html')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'busyness/order_list.html', {'orders': orders})


def create_question(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.answer = ''  # Убедитесь, что ответ пустой при создании вопроса
            faq.save()
            return redirect('busyness:faq_list')
    else:
        form = FAQForm()
    return render(request, 'busyness/create_question.html', {'form': form})

# Представление для отображения списка вопросов и ответов
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'busyness/faq_list.html', {'faqs': faqs})

def faq_detail(request, faq_id):
    # Получаем конкретный вопрос или выводим 404, если он не найден
    faq = get_object_or_404(FAQ, id=faq_id)
    return render(request, 'busyness/faq_detail.html', {'faq': faq})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        product = Product.objects.get(id=product_id)
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        cart_item.quantity += int(quantity)
        cart_item.save()
        return redirect('/')

def view_cart(request):
    user = request.user
    if user.is_authenticated and user.is_customer:
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.all()
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'busyness/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        return redirect('/')
    
def remove_from_cart(request, cart_item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
        cart_item.delete()
        return redirect('busyness:cart')
    return redirect('/')
    
def search_products(request):
    query = ""
    results = []
    
    if 'query' in request.GET:
        query = request.GET['query']
        results = Product.objects.filter(name__icontains=query)
    
    return render(request, 'busyness/search_results.html', {
        'query': query,
        'results': results
    })
    
    
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('/', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'busyness/add_review.html', {'form': form, 'product': product})


def add_promo_code(request):
    if request.method == 'POST':
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Перенаправляем на страницу админ-панели
    else:
        form = PromoCodeForm()
    return render(request, 'busyness/add_promo_code.html', {'form': form})

def apply_promo_code(request):
    if request.method == 'POST':
        code = request.POST.get('promo_code')
        try:
            promo_code = PromoCode.objects.get(code=code, is_active=True)
            if not UsedPromoCode.objects.filter(user=request.user, promo_code=promo_code).exists():
                cart = Cart.objects.get(user=request.user)
                discount = promo_code.discount
                total_price = sum(item.product.price * item.quantity for item in cart.cartitem_set.all())
                discounted_price = total_price * (1 - discount / 100)

                # Создаем запись о том, что промокод был использован
                UsedPromoCode.objects.create(user=request.user, promo_code=promo_code)

                logger.info(f"Promo code '{promo_code.code}' applied successfully by user {request.user.username}.")
                return render(request, 'busyness/cart.html', {
                    #'cart_items': cart.cartitem_set.all(),
                    'total_price': total_price,
                    'discounted_price': discounted_price,
                    'promo_code': promo_code,
                    'success': True
                })
            else:
                logger.warning(f"User {request.user.username} has already used promo code '{promo_code.code}'.")
                cart_items = Cart.objects.get(user=request.user).cartitem_set.all()
                total_price = sum(item.product.price * item.quantity for item in cart_items)
                return render(request, 'busyness/cart.html', {
                    'cart_items': cart_items,
                    'total_price': total_price,
                    'error': 'You have already used this promo code.'
                })
        except PromoCode.DoesNotExist:
            logger.error(f"Invalid promo code '{code}' entered by user {request.user.username}.")
            cart_items = Cart.objects.get(user=request.user).cartitem_set.all()
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            return render(request, 'busyness/cart.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'error': 'Invalid promo code.'
            })
    else:
        form = PromoCodeForm()
    return render(request, 'busyness/apply_promo_code.html', {'form': form})

def promo_code_list(request):
    promo_codes = PromoCode.objects.all()
    return render(request, 'busyness/promo_code_list.html', {'promo_codes': promo_codes})











@login_required
def confirm_order(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = cart.cartitem_set.all()

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    promo_code = request.session.get('promo_code', None)
    if promo_code:
        promo_code_obj = PromoCode.objects.get(code=promo_code)
        discount = promo_code_obj.discount
        discounted_price = total_price * (1 - discount / 100)
        total_price = discounted_price

    for item in cart_items:
        if item.quantity > item.product.stock:
            logger.error(request, f"Not enough stock for {item.product.name}")
            return redirect('busyness:cart')

    # Создаем платеж с PayPal
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('busyness:payment_execute')),
            "cancel_url": request.build_absolute_uri(reverse('busyness:payment_cancel'))
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": item.product.name,
                    "sku": item.product.id,
                    "price": str(item.product.price),
                    "currency": "USD",
                    "quantity": item.quantity
                } for item in cart_items]
            },
            "amount": {
                "total": str(total_price),
                "currency": "USD"
            },
            "description": "Order from busyness"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = link.href
                return HttpResponseRedirect(approval_url)
    else:
        print(payment.error)
        logger.error(request, "Error while creating PayPal payment")
        return redirect('busyness:cart')

@login_required
def payment_execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = cart.cartitem_set.all()

        total_price = sum(item.product.price * item.quantity for item in cart_items)

        promo_code = request.session.get('promo_code', None)
        if promo_code:
            promo_code_obj = PromoCode.objects.get(code=promo_code)
            discount = promo_code_obj.discount
            discounted_price = total_price * (1 - discount / 100)
            total_price = discounted_price

        # Create Order
        sale = Sale.objects.create(user=user, total_price=total_price, promo_code=promo_code_obj if promo_code else None)

        for item in cart_items:
            SaleItem.objects.create(sale=sale, product=item.product, quantity=item.quantity, price=item.product.price)
            item.product.stock -= item.quantity
            item.product.save()

        # Clear the cart
        cart.cartitem_set.all().delete()
        
        logger.info(request, "Order confirmed successfully!")
        return redirect('busyness:order_success')
    else:
        logger.error(request, "Error while executing PayPal payment")
        return redirect('busyness:cart')

@login_required
def payment_cancel(request):
    logger.info(request, "Payment was cancelled")
    return redirect('busyness:cart')



def multimode(data):
    """
    Возвращает список самых часто встречающихся значений в наборе данных.
    Если список мод содержит только одно значение, оно будет возвращено.

    Args:
        data: Итерируемый объект, содержащий данные для анализа.

    Returns:
        list: Список мод или пустой список, если data пуст.
    """
    if not data:
        return []

    # Подсчитываем количество вхождений каждого значения
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1

    # Находим максимальное количество вхождений
    max_count = max(counts.values())

    # Создаем список мод
    modes = [value for value, count in counts.items() if count == max_count]

    return modes



@login_required
def statistics_view(request):
    customers = Customer.objects.all().order_by('user__username')
    products = Product.objects.all().order_by('name')
    total_sales = Sale.objects.filter(is_paid=True).aggregate(total=Sum('total_price'))['total'] or 0
    sales_amounts = list(Sale.objects.filter(is_paid=True).values_list('total_price', flat=True))

    # Статистические показатели по сумме продаж
    mean_sales = statistics.mean(sales_amounts) if sales_amounts else 0
    median_sales = statistics.median(sales_amounts) if sales_amounts else 0
    mode_sales_list = multimode(sales_amounts)
    mode_sales = mode_sales_list[0] if mode_sales_list else 0

    # Возраст клиентов для расчетов статистики
    ages = [customer.user.age for customer in customers if customer.user.age is not None]

    # Статистические показатели по возрасту клиентов
    mean_age = statistics.mean(ages) if ages else 0
    median_age = statistics.median(ages) if ages else 0
    
    # Генерация графиков
    pie_chart = generate_pie_chart()
    histogram = generate_histogram()

    context = {
        'customers': customers,
        'products': products,
        'total_sales': total_sales,
        'mean_sales': mean_sales,
        'median_sales': median_sales,
        'mode_sales': mode_sales,
        'mean_age': mean_age,
        'median_age': median_age,
        'pie_chart': pie_chart,
        'histogram': histogram,
    }

    return render(request, 'busyness/statistics.html', context)

def generate_pie_chart():
    # Получение данных о продажах продуктов
    products = Product.objects.all()
    sales_data = {}
    for product in products:
        total_sales = SaleItem.objects.filter(product=product).aggregate(total=Sum('quantity'))['total']
        if total_sales:
            sales_data[product.name] = total_sales

    labels = list(sales_data.keys())
    sizes = list(sales_data.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Убедиться, что круговая диаграмма является кругом

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()

    return base64.b64encode(image_png).decode('utf-8')

def generate_histogram():
    customers = Customer.objects.all()
    ages = [customer.user.age for customer in customers if customer.user.age is not None]

    fig, ax = plt.subplots()
    ax.hist(ages, bins=np.arange(10, 101, 10), edgecolor='black')
    ax.set_xlabel('Age')
    ax.set_ylabel('Number of Customers')
    ax.set_title('Distribution of Customers by Age')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()

    return base64.b64encode(image_png).decode('utf-8')
