from django.urls import path

from drinks.views import *


urlpatterns = [
    path("thumbsup/",thumbsup,name='thumbsup'),
    path("maaza/",maaza,name='maaza'),
]
