from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
    context = {"listings" : listings}
    return render(request, 'pages/index.html', context)


def about(request):
    realtors_base = Realtor.objects.all()
    realtors = realtors_base.order_by('-hire_date')
    mvp_realtors = realtors_base.filter(is_mvp=True)
    context = {"realtors" : realtors, "mvp_realtors" : mvp_realtors}
    return render(request,'pages/about.html', context)


