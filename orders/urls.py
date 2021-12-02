from django.urls import path
from .views import OrderCreateView
app_name = 'orders'

urlpatterns = [
    path('place-order/', OrderCreateView.as_view(), name='order_create')
]
