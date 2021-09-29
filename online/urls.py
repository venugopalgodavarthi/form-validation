from django.urls import path
from online import views

urlpatterns=[
    path('',views.registerview,name="registerview")
    ]