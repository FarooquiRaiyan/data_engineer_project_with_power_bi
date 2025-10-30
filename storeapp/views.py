from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.db.models import Sum
from django.core.paginator import Paginator

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form':form})

# def product_list(request):
#     products = Product.objects.all()
#     total_price = products.aggregate(Sum('price'))['price__sum'] or 0
#     return render(request, 'product_list.html',{'products':products, 'total_price':total_price})

def product_list(request):
    product_list = Product.objects.all().order_by('-id')  # latest added
    paginator = Paginator(product_list, 15)  # 15 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    total_price = product_list.aggregate(Sum('price'))['price__sum'] or 0

    return render(request, 'product_list.html', {
        'products': products,
        'total_price': total_price
    })
