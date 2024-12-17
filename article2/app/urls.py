from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('one/<int:prk>',views.details,name="details")
    
]