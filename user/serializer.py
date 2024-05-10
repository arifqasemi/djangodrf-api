from rest_framework import serializers
from user.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
      class Meta:
        model = Customer
        fields =['first_name','last_name','email','password']