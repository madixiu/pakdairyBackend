# pak/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,ProductcategoryDetail

router = DefaultRouter()
router.register(r'products', ProductViewSet)
# router.register(r'productscategory', ProductcategoryDetail)

urlpatterns = [
    path('', include(router.urls)),
    path('productscategory/', ProductcategoryDetail.as_view(), name='productcategory-list'),

]