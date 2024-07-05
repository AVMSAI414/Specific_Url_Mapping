from django.urls import path
from food.views import *

app_name="food"


urlpatterns = [
    path("biryani/",biryani,name='biryani'),
    path("dosa/",dosa,name='dosa'),
]
