from django.urls import path
from . import views
app_name = 'showcase'
urlpatterns = [
    path('', views.main_showcase, name='main_showcase'),
]
