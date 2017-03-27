from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name='sales'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^item/(?P<product_id>[0-9]+)/$', views.item_detail, name='itemDetail'),
	url(r'^item/(?P<product_id>[0-9]+)/add_to_cart/$', views.add_to_cart, name='addToCart'),
	url(r'^shopping_cart/$', views.checkout, name='checkout'),
    url(r'^charge/(?P<amount>[0-9]+)/$', views.charge, name='charge'),
]