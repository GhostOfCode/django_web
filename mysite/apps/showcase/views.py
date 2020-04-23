from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(requset):
    return render(requset, 'showcase/index.html', {})
