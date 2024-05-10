from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import Customer
from user.serializer import CustomerSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here

class LoginView(APIView):
    def get(self,request):
        try:
            customers = Customer.objects.all()
            customer_serializer = CustomerSerializer(customers,many=True)
            return Response({'some data':customer_serializer.data})
        except Customer.DoesNotExist:
            return Response({'error': 'Customer with this email does not exist'}, status=404)
        
    def post(self,request):
            email = request.data.get('email')
            password = request.data.get('password')
            
            if email and password:
                user = authenticate(email=email,password=password)
                if user is not None:
                    token,create = Token.objects.get_or_create(user=user)
                    return Response({'message':'you are logged in successfully!','token': token.key})
                else:
                    return Response({' the data is not valid'})
            else:
                return Response({'the email and passowrd is required'})
       
    
    


class SignUpView(APIView):
    
    def post(self,request):
        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            user = customer_serializer.save()
            user.set_password(request.data['password'])
            user.first_name = 'test'
            user.last_name = 'test'
            user.is_admin = True
            user.save()

            return Response({'message':'the user has been created succefully!','data':customer_serializer.data})
        else:
            return Response({'error':customer_serializer.errors})