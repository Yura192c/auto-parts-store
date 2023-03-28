from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None, subcategory_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    sub_categories = SubCategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # if subcategory_slug:
        #     subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        #     products = products.filter(subcategory=subcategory)

        # subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        # products = products.filter(category=subcategory)
        sub_categories = SubCategory.objects.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'sub_categories': sub_categories})


def product_list_by_subcategory(request, category_slug = None, subcategory_slug=None):
    category = None
    categories = Category.objects.all()
    subcategory = None
    subcategories = SubCategory.objects.all()
    products = Product.objects.filter(available=True)
    if subcategory_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        products = products.filter(category=subcategory)
    return render(request,
                  'shop/product/product_list_by_category.html',
                  {'category': category,
                   'categories': categories,
                   'subcategory': subcategory,
                   'sub_categories': subcategories,
                   'products': products})

                   
def product_detail(request,category_slug = None, subcategory_slug=None, id=None, slug=None):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

#def shop_home(request):
 #   return render(request,'shop/product/list.html')

#def shop_home(request):
 #   return render(request,'shop/shop_home.html')