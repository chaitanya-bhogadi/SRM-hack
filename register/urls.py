from django.urls import  path,include
from . import views
from django.conf.urls import url



urlpatterns = [

    path('',views.register,name="register"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name="activate"),
]