from django.shortcuts import render
from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.
# def product_create_view(request):
#     my_form = RawProductForm()  # default -> request.GET
#     # password = ProductForm()  # creating multiple form Password-Form as well as Product-Form
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # Corrected data to be input
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#         # 'password': password,
#     }
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
# print(request.GET)
# print(request.POST)
# if request.method == 'POST':
#    ny_new_title = request.POST.get('title')
#    print(ny_new_title)
#    Product.objects.create(title = my_new_title)
# context = {}
# return render(request, 'products/product_create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #   'title': obj.title,
    #    'description': obj.description,
    #    'price': obj.price,
    #    'summary': obj.summary,
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
