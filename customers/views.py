from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.http import HttpResponse
import csv
import json
from django.views.generic import ListView,DetailView



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    logs = getattr(customer, 'logs', None)
    if logs:
        logs = logs.order_by('-timestamp')[:10]
    return render(request, 'customers/customers_detail.html', {'customer': customer, 'logs': logs})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customers_detail.html', {'form': form, 'customer': None})


def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customers/customers_detail.html', {'form': form, 'customer': customer})


def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customer_list')
    return render(request, 'customers/customers_detail.html', {'customer': customer})


def export_data(request):
    file_type = request.GET.get('file_type')
    if file_type == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="customers.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID','FULL NAME','EMAIL','PHONE NUMBER','ADDRESS','JOINED'])

        customers = Customer.objects.all().values_list('id','full_name','email','phone','address','joined')
        for customer in customers:
            writer.writerow(customer)

        return response

    elif file_type == 'json':
        response = HttpResponse(content_type='application/json')
        data = list(Customer.objects.all().values('id','full_name', 'email', 'phone', 'address','joined'))
        response.write(json.dumps(data, indent=4,default=str))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
        return response
    
    elif file_type == 'excel':
        response = HttpResponse(content_type='text/tab-separated=values')
        response['Content-Dispoition'] = 'attachment; filename="customers.xls"'

        writer = csv.writer(response, delimiter='\t')
        writer.writerow(['ID', 'FULL_NAME', 'EMAIl', 'PHONE NUMBER', 'ADDRESS', 'JOINED'])

        customers = Customer.objects.all().values_list('id', 'full_name', 'email', 'phone', 'address', 'joined')
        for customer in customers:
            writer.writerow(customer)

        return response