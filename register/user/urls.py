from django.urls import path
# from . import views

from .views import (
    ItemDetailView,
    home,
    HomeView,
    signup,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    login,
    OrderSummaryView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', signup, name = 'signup'),
    path('login', login, name = 'login'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
        name='remove-single-item-from-cart'),
]