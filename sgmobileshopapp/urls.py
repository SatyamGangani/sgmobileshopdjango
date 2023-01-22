from django.urls import path
from sgmobileshopapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.about,name='about'),
    path('products',views.product,name='products'),
    path('products/<slug:slug>',views.product_filter,name='ProductDetail'),
]