from django.urls import path
from . import views

# cai nay la chi nhin vao urls store k nhin vao urls khac.
# tuong ung voi cai urls trong setting
app_name = 'store'
urlpatterns = [
    path('', views.all_product, name='all_products')
]