from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'busyness'

urlpatterns = [
    path('add_product/', views.add_product),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('edit_product/<int:id>', views.update_product, name='edit_product'),
    path('add_news/', views.add_news, name='add_news'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('new/<int:id>/', views.new_detail, name='new_detail'),
    path('delete_news/<int:id>/', views.delete_news, name='delete_news'),
    path('edit_news/<int:id>/', views.edit_news, name='edit_news'),
    path('read_all_new/<int:id>/', views.read_all_new, name='read_all_new'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('edit_supplier/<int:id>/', views.edit_supplier, name='edit_supplier'),
    path('delete_supplier/<int:id>/', views.delete_supplier, name='delete_supplier'),
    path('supplier_list/', views.supplier_list, name='supplier_list'),
    path('suppliers/', views.employees_suppliers),
    path('check_products/<int:supplier_id>/', views.check_products, name='check_products'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('order_list/', views.order_list, name='order_list'),
    path('faq_list/', views.faq_list, name='faq_list'),
    path('faq_detail/<int:faq_id>/', views.faq_detail, name='faq_detail'), 
    path('create_question/', views.create_question, name='create_question'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('search/', views.search_products, name='search_products'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_promo_code/', views.add_promo_code, name='add_promo_code'),
    path('promo_code_list/', views.promo_code_list, name='promo_code_list'), 
    path('cart/apply_promo_code/', views.apply_promo_code, name='apply_promo_code'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    re_path(r'^payment/execute/$', views.payment_execute, name='payment_execute'),
    re_path(r'^payment/cancel/$', views.payment_cancel, name='payment_cancel'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('news_list/', views.news_list, name='news_list'),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)