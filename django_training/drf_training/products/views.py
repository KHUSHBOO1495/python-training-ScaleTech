# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Product
# from .serializers import ProductSerializer

# class ProductList(APIView):
#     """
#     API view for listing and creating products.
#     """

#     def get(self, request):
#         """
#         Return all products.
#         """

#         products = Product.objects.all()

#         serializer = ProductSerializer(products, many=True)

#         return Response(serializer.data)



from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]