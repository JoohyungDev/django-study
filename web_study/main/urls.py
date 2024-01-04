# from django.urls import path

# from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path
from .views import *

app_name='main'

urlpatterns=[
    path('',index),
    path('blog/',blog),
]
