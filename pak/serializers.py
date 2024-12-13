# pak/serializers.py

import base64
from rest_framework import serializers
from .models import Product
from .models import Productcategory

class ProductSerializer(serializers.ModelSerializer):
    picture_base64 = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'code',
            'categorycode',
            'pagecode',
            'brandcode',
            'fname',
            'ename',
            'fsummary',
            'esummary',
            'fdescription',
            'edescription',
            'picture',
            'ordernum',
            'active',
            'price',
            'topnew',
            'newproduct',
            'picture_base64',  # Add the new field here
        ]

    def get_picture_base64(self, obj):
        if obj.picture:
            return base64.b64encode(obj.picture).decode('utf-8')  # Convert bytes to base64
        return None
    


class ProductcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Productcategory
        fields = '__all__'  # or specify the fields you want to include