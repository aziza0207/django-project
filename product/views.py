from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AddToWishListView(generics.GenericAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        in_wishlist = Product.objects.filter(wishlist__id=request.user.id, pk=product.id).exists()
        if in_wishlist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        product.wishlist.add(request.user)
        return Response(status=status.HTTP_200_OK, data={"message": "Added to WishList"})


class RemoveFromWishListView(generics.GenericAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        in_wishlist = Product.objects.filter(wishlist__id=request.user.id, pk=product.id).exists()
        if not in_wishlist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        product.wishlist.remove(request.user)
        return Response(status=status.HTTP_200_OK, data={"message": "Removed from WishList"})


class UsersWishList(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(wishlist=self.request.user.id)
