from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('one/<int:pk>',details,name='details'),
]