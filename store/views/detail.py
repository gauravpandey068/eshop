from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category



def detail(request, id):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('?')
    product = Product.objects.get(id=id)
    context = {
        'categories': categories,
        'products': products,
        'product': product,
    }
    return render(request, 'detail.html', context)
