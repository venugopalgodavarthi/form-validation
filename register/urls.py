from django.urls import path
from register import views 
urlpatterns=[
    path('',views.registerview,name="registerform")
]