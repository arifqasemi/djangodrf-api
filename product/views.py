from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product
from product.serializer import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AllProductsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        products = Product.objects.all()
        product_serializer = ProductSerializer(products,many=True)
        return Response({'the view from the all products view':product_serializer.data})