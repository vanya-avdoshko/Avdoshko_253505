from django.contrib import admin
from .models import Product, Employee, Supplier, Category, Sale, Article, News,  Order, OrderProduct, FAQ, Vacancy, Review, PromoCode, UsedPromoCode, Sale, SaleItem, Company, Partner, SliderSettings

admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Article)
admin.site.register(News)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(FAQ)
admin.site.register(Vacancy)
admin.site.register(Review)
admin.site.register(PromoCode)
admin.site.register(UsedPromoCode)
admin.site.register(Company)
admin.site.register(Partner)
admin.site.register(SliderSettings)

