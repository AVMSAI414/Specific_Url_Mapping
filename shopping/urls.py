from django.urls import path
from shopping.views import *

urlpatterns = [
    path("shirts/",shirts,name='shirts'),
    path("jeans/",jeans,name='jeans'),
]
