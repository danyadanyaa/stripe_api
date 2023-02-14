from django.urls import path
from .views import OneItemCheckout, ItemPage

from . import views

urlpatterns = [
    path('config/', views.stripe_config),
    path('item/<int:id>/', ItemPage.as_view(), name="item"),
    path('buy/<int:id>/', OneItemCheckout.as_view(), name='checkout_session')
    ]