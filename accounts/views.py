from django.shortcuts import render,redirect

from .models import *

from .forms import *
# Create your views here.

def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders,'delivered':delivered,
    'pending':pending }
    return render(request,'dashboard.html',context)

def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products':products})


def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request,'customer.html',context)

def add_product(request):
    context={}
    return render(request,'add_product.html',context)

def create_order(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'create_order.html',context)