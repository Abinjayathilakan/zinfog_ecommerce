from django.shortcuts import render, redirect
from . models import Product
from django.core.paginator import Paginator
import os
# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    print(context)
    return render(request,'index.html',context)

def list_products(request):
    """_summary_
    returns product list page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list = Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context = {'products': product_list}
    return render(request, 'products.html', context)


def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}


    return render(request,'product_detail.html',context)


# def shop_customerList(request):
#     docdb=Customer.objects.all()
#     return render(request, 'shop_banner.html',{'doc':docdb})

def show_products(request):
    docdb=Product.objects.all()
    return render(request, 'customer_banner.html',{'doc':docdb})



def product(request):
    return render(request, 'add_products.html')


def add_details(request):
    if request.method == "POST":
        pname = request.POST.get('tile')
        price = request.POST.get('Product_price')
        des = request.POST.get('Description')
        image=request.FILES.get('file')
        product = Product(title=pname, description=des, price=price, image=image)
        product.save()
        return redirect('show_products')
    
def edit_product(request,ab):
    prod=Product.objects.get(id=ab)
    return render(request,'edit_product.html',{'product':prod})



def edit_product_details(request, ab):
    product = Product.objects.get(id=ab)
    
    if request.method == 'POST':
        if request.FILES.get('file'):
            # Delete old image if a new one is uploaded
            if product.image:
                os.remove(product.image.path)
            product.image = request.FILES.get('file')

        product.title = request.POST.get('tile')
        product.price = request.POST.get('Product_price')
        product.description = request.POST.get('Description')
        product.save()

        return redirect('show_products')
    
    return render(request, 'edit_product.html', {'product': product})

    
def delete_product(request,ab):
    product_details=Product.objects.get(id=ab)
    product_details.delete()
    return redirect('show_products')
    


