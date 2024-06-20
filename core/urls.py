from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'inventory_items', InventoryItemViewSet, basename='inventory_items')
router.register(r'suppliers', SuppliersViewSet, basename='suppliers')
urlpatterns = router.urls