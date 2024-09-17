"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include , path
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('rackets/', rackets, name='rackets'),
    path('rackets/yonex/', yonex, name='yonex'),
    path('rackets/victor/', victor, name='victor'),
    path('shoes/', shoes, name='shoes'),
    path('shoes/sh_yonex/', shoes_yonex, name='sh_yonex'),
    path('shoes/sh_victor/', shoes_victor, name='sh_victor'),
    path('accessories/', accessories, name='accessories'),
    path('bag/', bag, name='bag'),
    path('bag_yonex/', bag_yonex, name='bag_yonex'),
    path('bag_victor/', bag_victor, name='bag_victor'),
    path('grips/', grips, name='grips'),
    path('signup/', signup, name='signup'),
    path('wristband/', wristband, name='wristband'),
    path('headband/', headband, name='headband'),
    path('socks/', socks, name='socks'),
    path('cushion/', cushion, name='cushion'),
    path('towel/', towel, name='towel'),
    path('signup/addUser', addUser, name='addUser'),
    path('login/', login, name='login'),
    path('login/loginForm', loginForm, name='loginForm'),
    path('logout/', logout, name='logout'),
    path('cart/', cart, name='cart'),
    path('del_cart_item/<product_id>', del_cart_item, name='del_cart_item'),
    path('checkout/', checkout, name='checkout'),
    path('addtocart/<product_id>', addtocart, name='addtocart'),
    path('product_list/', product_list, name='product_list'),
    path('info/<product_id>', info, name='info'),
    path('checkout/', checkout, name='checkout'),
    path('showMyorder/', showMyorder, name='showMyorder'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
