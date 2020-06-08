from django.urls import path


from supple.views import *

urlpatterns=[
    path("",home),
    path("register/",register),
    path("signin/",signin),
    path("store/",store),
    path('logout/',signout),
    path('contactus/',contactus),
    path('about/',about),
    path('ask/',ask),
    path('cart/',cart),
    path('order/',order),
    path('shipping/',shipping)
    
    
    
]