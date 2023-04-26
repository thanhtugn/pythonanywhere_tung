from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer

def listing(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list, 5)

    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'list.html',{'customers' : customers})