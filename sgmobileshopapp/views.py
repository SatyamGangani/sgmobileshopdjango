from django.shortcuts import render,HttpResponse
from sgmobileshopapp.models import Brand,Product,Category

# Create your views here.
def index(request):
    data={
        'brands': [brand for brand in  Brand.objects.all()]
    }
    return render(request,'index.html',data)
def about(request):
    return render(request,'aboutus.html')
    # return HttpResponse("hello")
def product(request):
    
    data = {
        'products' : [product for product in Product.objects.all()] 
    }
    return render(request,'products.html',data)

def products_detail(request,product_id):
    print(product_id)
    data = {
        'products' : [product for product in Product.objects.all()] 
    }
    return render(request,'products.html',data)

def product_filter(request,slug):
    print(slug)
    category = Category.objects.filter(slug=slug)[0].name
    data = {
        "products" : [product for product in Product.objects.filter(category_id=category)]
    }
    return render(request,'products.html',data)
    # return HttpResponse('')