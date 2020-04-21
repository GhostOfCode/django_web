from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def main_showcase(request):
    return render(request, 'showcase/main_landing.html', {})
