from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    form = SubscriberForm(request.POST or None)
    return render(request, 'landing/landing.html', {'form': form})
