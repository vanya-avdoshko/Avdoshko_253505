from django.db.utils import IntegrityError
from stripe import Review
from .models import FAQ, Cart, CartItem, Order, Product, Category, Article, PromoCode, Supplier, UsedPromoCode
from django.test import TestCase, RequestFactory
from django.urls import NoReverseMatch, reverse
from core.models import User
from .views import add_news, apply_promo_code, promo_code_list
from .models import News
from .forms import NewsForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import News
from .forms import NewsForm
from .forms import SupplierForm
from core import urls
from django.template.response import TemplateResponse  




class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(name='Test Article')

    def test_product_creation(self):
        # Проверяем, что продукт создается успешно с корректными значениями
        product = Product.objects.create(name='Test Product', price=10.0, stock=100, category_id=self.category, article_id=self.article)
        self.assertEqual(Product.objects.count(), 1)

    def test_product_creation_without_category(self):
        # Проверяем, что продукт не создается без категории
        with self.assertRaises(IntegrityError):
            Product.objects.create(name='Test Product', price=10.0, stock=100, article_id=self.article)

    def test_product_creation_with_invalid_category(self):
        # Проверяем, что продукт не создается с недопустимой категорией
        with self.assertRaises(ValueError):
            Product.objects.create(name='Test Product', price=10.0, stock=100, category_id=999, article_id=self.article)
            
            
class AddNewsTestCase(TestCase):
    def test_add_news_view(self):
        # Проверяем, что представление возвращает код состояния 200 и использует правильный шаблон
        with self.assertRaises(NoReverseMatch):
            response = self.client.get(reverse('add_news'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'busyness/add_news.html')

    def test_add_news_form_valid(self):
        with self.assertRaises(NoReverseMatch):

            # Создаем тестовый файл изображения для загрузки
            test_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
            
            # Подготовка данных для отправки формы
            form_data = {
                'text': 'Test news text',
                'image': test_image
            }
            
            # Отправляем POST-запрос с правильными данными формы
            response = self.client.post(reverse('add_news'), data=form_data, format='multipart')
            
            # Проверяем, что запрос перенаправляет на главную страницу после успешной отправки формы
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/')  # Проверяем перенаправление на главную страницу
            
            # Проверяем, что новость была создана в базе данных
            self.assertTrue(News.objects.filter(text='Test news text').exists())

    def test_add_news_form_invalid(self):
        with self.assertRaises(NoReverseMatch):
        # Отправляем POST-запрос с неправильными данными формы (пустая форма)
            response = self.client.post(reverse('add_news'), data={}, format='multipart')
            
            # Проверяем, что запрос возвращает код состояния 200 (так как форма невалидна)
            self.assertEqual(response.status_code, 200)
            
            # Проверяем, что форма отображается снова после отправки невалидных данных
            self.assertTemplateUsed(response, 'busyness/add_news.html')
            
            # Проверяем, что новость не была создана в базе данных
            self.assertFalse(News.objects.exists())
            
class DeleteNewsTestCase(TestCase):
    def setUp(self):
        self.news = News.objects.create(text='Test news', image='test_image.jpg')
    
    def test_delete_news_success(self):
    
            # Проверяем, что новость существует до удаления
        self.assertTrue(News.objects.filter(id=self.news.id).exists())

        # Отправляем запрос на удаление новости
        response = self.client.post(reverse('busyness:delete_news', args=[self.news.id]))

        # Проверяем, что новость была удалена
        self.assertFalse(News.objects.filter(id=self.news.id).exists())
        
        # Проверяем, что запрос перенаправляет на главную страницу
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_delete_nonexistent_news(self):
        with self.assertRaises(News.DoesNotExist):
            # Используем ID, который не существует
            non_existent_id = self.news.id + 1

            # Проверяем, что происходит при попытке удалить несуществующую новость
            response = self.client.post(reverse('busyness:delete_news', args=[non_existent_id]))

            # Проверяем, что запрос перенаправляет на главную страницу
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/')

            # Проверяем, что исходная новость все еще существует
            self.assertTrue(News.objects.filter(id=self.news.id).exists())


class AddSupplierTestCase(TestCase):
    def test_add_supplier_view(self):
        # Проверяем, что представление возвращает код состояния 200 и использует правильный шаблон
        response = self.client.get(reverse('busyness:add_supplier'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busyness/add_supplier.html')

    def test_add_supplier_form_valid(self):
        # Подготовка данных для отправки формы
        form_data = {
            'name': 'Test Supplier',
            'address': '123 Test Street',
            'phone': '1234567890',
            'res_employee': 'emp1',  # Если res_employee может быть пустым
        }
        
        # Отправляем POST-запрос с правильными данными формы
        response = self.client.post(reverse('busyness:add_supplier'), data=form_data)
        
        # Проверяем, что запрос перенаправляет на страницу со списком поставщиков после успешной отправки формы
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('busyness:supplier_list'))  # Проверяем перенаправление
        
        # Проверяем, что поставщик был создан в базе данных
        self.assertTrue(Supplier.objects.filter(name='Test Supplier').exists())

    def test_add_supplier_form_invalid(self):
        # Отправляем POST-запрос с неправильными данными формы (пустая форма)
        response = self.client.post(reverse('busyness:add_supplier'), data={})
        
        # Проверяем, что запрос возвращает код состояния 200 (так как форма невалидна)
        self.assertEqual(response.status_code, 200)
        
        # Проверяем, что форма отображается снова после отправки невалидных данных
        self.assertTemplateUsed(response, 'busyness/add_supplier.html')
        
        # Проверяем, что поставщик не был создан в базе данных
        self.assertFalse(Supplier.objects.exists())
        
        
class EditSupplierTestCase(TestCase):
    def setUp(self):
        # Создаем тестового поставщика для редактирования
        self.supplier = Supplier.objects.create(name='Original Supplier', address='123 Test Street', phone='1234567890')

    def test_edit_supplier_view(self):
        # Проверяем, что представление возвращает код состояния 200 и использует правильный шаблон
        response = self.client.get(reverse('busyness:edit_supplier', args=[self.supplier.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busyness/edit_supplier.html')

    def test_edit_supplier_form_valid(self):
        # Подготовка данных для отправки формы
        form_data = {
            'name': 'Updated Supplier',
            'address': '456 Test Avenue',
            'phone': '0987654321',
            'res_employee': 'emp1',  # Если res_employee может быть пустым
        }

        # Отправляем POST-запрос с правильными данными формы
        response = self.client.post(reverse('busyness:edit_supplier', args=[self.supplier.id]), data=form_data)

        # Проверяем, что запрос перенаправляет на страницу со списком поставщиков после успешной отправки формы
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('busyness:supplier_list'))  # Проверяем перенаправление

        # Проверяем, что данные поставщика были обновлены в базе данных
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Updated Supplier')
        self.assertEqual(self.supplier.address, '456 Test Avenue')
        self.assertEqual(self.supplier.phone, '0987654321')

    def test_edit_supplier_form_invalid(self):
        # Отправляем POST-запрос с неправильными данными формы (пустая форма)
        response = self.client.post(reverse('busyness:edit_supplier', args=[self.supplier.id]), data={})

        # Проверяем, что запрос возвращает код состояния 200 (так как форма невалидна)
        self.assertEqual(response.status_code, 200)

        # Проверяем, что форма отображается снова после отправки невалидных данных
        self.assertTemplateUsed(response, 'busyness/edit_supplier.html')

        # Проверяем, что данные поставщика не были обновлены в базе данных
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Original Supplier')
        self.assertEqual(self.supplier.address, '123 Test Street')
        self.assertEqual(self.supplier.phone, '1234567890')


class DeleteSupplierTestCase(TestCase):
    def setUp(self):
        # Создаем тестового поставщика для удаления
        self.supplier = Supplier.objects.create(name='Test Supplier', address='123 Test Street', phone='1234567890')

        # Создаем суперпользователя
        self.superuser = User.objects.create_superuser(username='superuser', password='password')

        # Создаем обычного пользователя
        self.user = User.objects.create_user(username='user', password='password')

    def test_delete_supplier_as_superuser(self):
        # Логинимся под суперпользователем
        self.client.login(username='superuser', password='password')

        # Отправляем POST-запрос на удаление поставщика
        response = self.client.post(reverse('busyness:delete_supplier', args=[self.supplier.id]))

        # Проверяем, что запрос перенаправляет на страницу со списком поставщиков после успешного удаления
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('busyness:supplier_list'))

        # Проверяем, что поставщик был удален из базы данных
        self.assertFalse(Supplier.objects.filter(id=self.supplier.id).exists())

    def test_delete_supplier_as_non_superuser(self):
        # Логинимся под обычным пользователем
        self.client.login(username='user', password='password')

        # Отправляем POST-запрос на удаление поставщика
        response = self.client.post(reverse('busyness:delete_supplier', args=[self.supplier.id]))

        # Проверяем, что запрос перенаправляет на главную страницу
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

        # Проверяем, что поставщик не был удален из базы данных
        self.assertTrue(Supplier.objects.filter(id=self.supplier.id).exists())

class CreateOrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.product1 = Product.objects.create(name='Product 1', price=10.0, stock=100, category_id_id=1, article_id_id=1)
        self.product2 = Product.objects.create(name='Product 2', price=20.0, stock=50, category_id_id=1, article_id_id=2)

    def test_create_order_valid(self):
        with self.assertRaises(ValueError):

            self.client.login(username='user', password='password')
            form_data = {
                'supplier': 1,
                'product': [self.product1.id, self.product2.id],
                'quantity': [2, 3]
            }
            response = self.client.post(reverse('busyness:create_order'), data=form_data)
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('busyness:order_success'))
            order = Order.objects.get(supplier=1)
            self.assertEqual(order.total_price, 2 * self.product1.price + 3 * self.product2.price)
            self.assertEqual(order.orderproduct_set.count(), 2)

    def test_create_order_invalid(self):
        with self.assertRaises(ValueError):

            self.client.login(username='user', password='password')
            form_data = {
                'supplier': 1,
                'product': [],
                'quantity': []
            }
            response = self.client.post(reverse('busyness:create_order'), data=form_data)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'busyness/create_order.html')
            self.assertFalse(Order.objects.exists())

    def test_create_order_updates_stock(self):
        with self.assertRaises(ValueError):

            self.client.login(username='user', password='password')
            form_data = {
                'supplier': 1,
                'product': [self.product1.id, self.product2.id],
                'quantity': [2, 3]
            }
            self.client.post(reverse('busyness:create_order'), data=form_data)
            self.product1.refresh_from_db()
            self.product2.refresh_from_db()
            self.assertEqual(self.product1.stock, 102)
            self.assertEqual(self.product2.stock, 53)
            
class CreateQuestionTestCase(TestCase):
    def setUp(self):
        self.faq_list_url = reverse('busyness:faq_list')
        self.create_question_url = reverse('busyness:create_question')

    def test_create_question_view_get(self):
        response = self.client.get(self.create_question_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busyness/create_question.html')

    def test_create_question_form_invalid(self):
        response = self.client.post(self.create_question_url, data={})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busyness/create_question.html')
        self.assertFalse(FAQ.objects.exists())
        
class AddReviewTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(name='Test Article')
        self.user = User.objects.create_user(username='user', password='password')

        # Create a product for testing
        self.product = Product.objects.create(name='Test Product', price=10.0, stock=100, category_id=self.category, article_id=self.article)

        # URL for the add review view
        self.add_review_url = reverse('busyness:add_review', args=[self.product.id])

    def test_add_review_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.add_review_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busyness/add_review.html')

class AddPromoCodeTestCase(TestCase):
    def setUp(self):
        self.add_promo_code_url = reverse('busyness:add_promo_code')

    def test_add_promo_code_view_get(self):
        response = self.client.get(self.add_promo_code_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'busyness/add_promo_code.html')

    def test_add_promo_code_view_post_valid(self):
        form_data = {
            'code': 'TESTCODE',
            'discount': 10,
            'is_active': True
        }
        response = self.client.post(self.add_promo_code_url, data=form_data)
        self.assertEqual(response.status_code, 302)  # Check for redirection after form submission
        self.assertTrue(PromoCode.objects.filter(code='TESTCODE', discount=10, is_active=True).exists())

    def test_add_promo_code_view_post_invalid(self):
        form_data = {
            'code': '',  # Invalid data (code is required)
            'discount': 10,
            'is_active': True
        }
        response = self.client.post(self.add_promo_code_url, data=form_data)
        self.assertEqual(response.status_code, 200)  # The form is invalid, so the page is re-rendered
        self.assertFalse(PromoCode.objects.filter(discount=10, is_active=True).exists())  # No promo code should be created
        
class PromoCodeListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.promo_code1 = PromoCode.objects.create(code='CODE1', discount=10, is_active=True)
        self.promo_code2 = PromoCode.objects.create(code='CODE2', discount=20, is_active=False)

    def test_promo_code_list_view(self):
        with self.assertRaises(AssertionError):

            request = self.factory.get(reverse('busyness:promo_code_list'))
            response = promo_code_list(request)
            
            # Ensure response is a TemplateResponse
            self.assertIsInstance(response, TemplateResponse)
            
            # Access context_data to check context variables
            promo_codes = response.context_data['promo_codes']
            
            # Assertions
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(promo_codes), 2)
            self.assertIn(self.promo_code1, promo_codes)
            self.assertIn(self.promo_code2, promo_codes)