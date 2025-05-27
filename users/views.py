from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm, LoginForm, RegisterModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    logs = getattr(customer, 'logs', None)
    if logs:
        logs = logs.order_by('-timestamp')[:10]
    return render(request, 'users/customers_detail.html', {'customer': customer, 'logs': logs})



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'users/customers.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'users/customers_detail.html', {'form': form, 'customer': None})


def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('users:customer_list')
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'users/customers_detail.html', {'form': form, 'customer': customer})


def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('users:customer_list')
    return render(request, 'users/customers_detail.html', {'customer': customer})




def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(request,email = cd['email'],password = cd['password'])
            
            if user:
                login(request,user)
                return redirect('shop:home')
            else:
                messages.error(request, 'Username or Password incorrect')

            
    return render(request,'users/login.html',{'form':form})


def logout_page(request):
    logout(request)
    return redirect('shop:home')



def register_page(request):
    form = RegisterModelForm()
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('shop:home')
    return render(request, 'users/register.html', {'form': form})