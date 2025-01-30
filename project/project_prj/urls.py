from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='blog-home'),
    path('rasp', rasp, name='rasp'),
    path('news', news, name='news'),
    path('<int:pk>/delete', Del.as_view(), name='task-delete'),
    path('<int:pk>/update', Upd.as_view(), name='task-update'),
    path('orders/new/<int:pk>/', add_order, name='orders-create'),
    path('orders/<str:username>', UserOrdersListView.as_view(), name='orders-list'),
]
