from django.urls import path
from ruruB.views import index

urlpatterns = [
    path("", index, name="home"),

]