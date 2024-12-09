from django import forms
from .models import Product, News, PromoCode, Review, Supplier, Order, OrderProduct, FAQ, Vacancy

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category_id', 'article_id', 'image', 'supplier']
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','first_part','text', 'image']
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'phone']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier']

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']
        
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        
class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'description', 'image']
        
class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)])
        }       
        
        
class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'discount', 'is_active']
    
