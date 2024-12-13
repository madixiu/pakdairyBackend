# pak/views.py

from rest_framework import viewsets,generics
from .models import Product,Productcategory
from .serializers import ProductSerializer,ProductcategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductcategoryDetail(generics.ListCreateAPIView):
    queryset = Productcategory.objects.all()
    serializer_class = ProductcategorySerializer