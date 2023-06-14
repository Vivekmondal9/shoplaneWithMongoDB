from rest_framework import serializers
from .models import UserSignup,Products,Ratings


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserSignup
        fields="__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products        
        fields="__all__"