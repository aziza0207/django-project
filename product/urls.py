from django.urls import path, include
from rest_framework import routers
from .views import AddToWishListView, RemoveFromWishListView, UsersWishList, CategoryListView


router = routers.DefaultRouter()
router.register(r'wishlist', UsersWishList, basename='wishlist')

app_name = 'product'

urlpatterns = [path('category/', CategoryListView.as_view(), name='category'),
               path('add-product/<int:pk>', AddToWishListView.as_view(),
                    name='add-product'),
               path('remove-product/<int:pk>', RemoveFromWishListView.as_view(),
                    name='remove-product'),
               path('whishlist/', include(router.urls))]
