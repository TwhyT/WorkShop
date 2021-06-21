from django.db import connection
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Category, Collection, Product, ProductImage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    category = Category.objects.all()
    aqua = get_object_or_404(Product.objects.filter(name='SENSUAL AQUA LIPSTICK'))
    redvibe = get_object_or_404(Product.objects.filter(name='SENSUAL INTENSE VELVET'))
    return render(request, 'page/index.html',{
        'category':category,
        'aqua':aqua,
        'redvibe':redvibe,
    })

def productlist(request):
    product = None
    category = Category.objects.all()
    recommend = Product.objects.filter(recommend=True, published=True)
    categoryID = request.GET.get('category')
    search = request.GET.get('search')
    sort= request.GET.get('sort')
    product = Product.objects.filter(published=True)
    product = product.order_by('price','name')
    
    if categoryID:
        product = product.filter(category=categoryID)
        bred = category.get(id=categoryID)

    if search:
        product = product.filter(name__contains = search)
    # Sort
    if sort == 'asc':
        product = product.order_by('price')        
                        
    elif sort == 'desc':
        product = product.order_by('-price')
    
    paginator =Paginator(product,8)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    import sys
    print(product, file=sys.stderr)

    return render(request, 'laout/category.html',{
    'product' : product,
    'category' : category,
    'recommend':recommend,
    #Filter
    'categoryID' : categoryID if categoryID else '',
    'search' : search if search else '',
    'bred': bred if categoryID else 'All List',
    })

# Detail
def detail(request, slug):
    category = Category.objects.all()
    product = get_object_or_404(Product.objects.all(), code=slug)
    image = ProductImage.objects.all()
    image = image.filter(product = product)
    recommend = Product.objects.filter(recommend=True, published=True)
    bred = product.category
    cateoryID = product.category.id
    return render(request, 'laout/detail.html',{
        'product': product,
        'recommend' : recommend,
        'image' : image,
        'category': category,
        'bred': bred,
        'categoryID': cateoryID
    })

#Contact
def Contact(request):
    category = Category.objects.filter(published=True)
    form = ContactForm()
    if  request.method == 'POST':
        respon = request.POST.get('g-recaptcha-response')
        googlerecap = {
            'secret':'6LfQWzQbAAAAAEJLOBBfDZ9YOBy_Z4NGF9Rt6oHJ',
            'response':respon
        }
        recap = requests.post('https://www.google.com/recaptcha/api/siteverify', googlerecap)
        if recap.json()['success']:
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.published = True
                contact.save()
                form.save_m2m()
                messages.success(request, 'Save success')
                return HttpResponseRedirect(reverse('contact', kwargs={} ))
        else:
            messages.error(request, 'Save Failed')
    return render(request, 'page/contact.html',{
        'form': form,
        'category':category
    })

def about(request):
    return render(request, 'page/about.html')

# login signup
def login_view(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('productlist')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {
        'form':form,
        'category':category,
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
        

def signup_view(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('productlist')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {
        'form': form,
        'category':category,
        })