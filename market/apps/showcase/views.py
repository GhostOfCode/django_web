from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from ..products.models import ProductImage
from .forms import SubscriberForm


def index(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_form = form.save()
    return render(request, 'showcase/landing.html', locals())


def home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = ProductImage.objects.order_by('-updated')[:4]
    product_images_laptops = product_images.filter(product__category_id=1)
    product_images_phones = product_images.filter(product__category_id=2)
    product_images_accessories = product_images.filter(product__category_id=3)
    return render(request, 'showcase/home.html', locals())
