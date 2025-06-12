from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from tablib import Dataset
from django.http import HttpResponse, HttpResponseBadRequest



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


def export_customers(request):
    file_format = request.GET.get('format', 'csv')
    dataset = Dataset()
    dataset.headers = ['ID', 'Full Name', 'Email', 'Phone', 'Address', 'Joined']

    for customer in Customer.objects.all():
        dataset.append([
            customer.id,
            customer.full_name,
            customer.email,
            customer.phone,
            customer.address,
            customer.joined.strftime("%Y-%m-%d %H:%M")
        ])

    if file_format == 'csv':
        content = dataset.export('csv')
        content_type = 'test/csv'
        file_ext  ='csv'

    elif file_format == 'json':
        content = dataset.export('json')
        content_type = 'application/json'
        file_ext = 'json'

    elif file_format == 'xls':
        content = dataset.export('xls')
        content_type = 'application/vnd.excel'
        file_ext = 'xls'
    else:
        return HttpResponseBadRequest('Unsupported export format')
    
    response = HttpResponse(content, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="customers.{file_ext}"'
    return response