from django.urls import path
from apps.base.views import index,chef_detail,shop_detail



urlpatterns = [
    path ('', index, name= 'index'),
    path ('chef_detail/<int:id>/', chef_detail, name= 'chef_detail'),
    path ('shop_detail/<int:id>/', shop_detail, name= 'shop_detail')

]
