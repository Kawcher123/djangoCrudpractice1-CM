from django.shortcuts import render,redirect

from .models import *

from .forms import *
from django.forms import inlineformset_factory

from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'signup.html',context)

def login(request):
    context={}
    return render(request,'login.html',context)


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
    myfilter=OrderFilter(request.GET,queryset=orders)
    orders=myfilter.qs

    context = {'customer':customer, 'orders':orders, 'order_count':order_count,'myfilters':myfilter}
    return render(request,'customer.html',context)

def add_product(request):
    context={}
    return render(request,'add_product.html',context)

def create_order(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form=OrderForm(initial={'customer':customer})
    if request.method=='POST':
        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid:
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'create_order.html',context)

def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'create_order.html',context)


def delete_order(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')

    context={'order':order}
    return render(request,'delete_order.html',context)