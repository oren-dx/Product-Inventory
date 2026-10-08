from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from product_app.models import*


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        user_exist = UserModel.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(request, 'User already exists')
            return redirect('register')
        
        if password == conf_password:
            UserModel.objects.create_user(
                username = username,
                full_name = full_name,
                email = email,
                password= password,
            )
            messages.success(request, 'User created successfully')
            return redirect('login_page')
        else:
            messages.warning(request, 'Password doesnot match.')
            return redirect('register')

    return render(request, 'auth/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'User login successfully')
            return redirect('home_view')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('login_page')

    return render(request, 'auth/login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')


def home_view(request):
    search_filter =request.GET.get('Search_items')
    product_data = ProductDataModel.objects.all().order_by('-created_at')
    if search_filter:
        product_data = ProductDataModel.objects.filter(
            Q(name__icontains = search_filter)|
            Q(category__icontains = search_filter)
        )
        
        try:
            price = float(search_filter)
            search_query |= Q(price__gt=price)

        except ValueError:
            pass
        
    context ={
        'product_data': product_data,
    }
    return render(request, 'pages/home.html',context)


def product_list(request):
    
    products = ProductDataModel.objects.all().order_by('-created_at')
    status = request.GET.get('status')

    if status:
        products = products.filter(status=status)

    context = {
        'products': products,
        'status': status
    }
    return render(request, 'pages/product_list.html',context)

@login_required
def product_detail(request, id):

    product = get_object_or_404(ProductDataModel, id=id)
    
    context = {
        'product': product  
    }
    return render(request, 'pages/product_detail.html',context)



def add_product(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        image = request.FILES.get('image')
        status = request.POST.get('status')

        ProductDataModel.objects.create(
            name=name,
            category=category,
            price=price,
            qty=qty,
            image=image,
            status=status
        )

        return redirect('product_list')
    return render(request, 'pages/add_product.html')

@login_required
def product_update(request,p_id):
    
    product = ProductDataModel.objects.get(id = p_id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.brand = request.POST.get('brand')
        product.price = request.POST.get('price')
        product.qty = request.POST.get('qty')
        product.status = request.POST.get('status')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        return redirect('Product_list')
    
    context ={
        'product':product
    }
    return render(request, 'pages/product_update.html',context)

@login_required
def product_delete(request,p_id):
    ProductDataModel.objects.get(id = p_id).delete()
    return redirect('Product_list')
    

