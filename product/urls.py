from django.urls import path, include
from rest_framework import routers
from .views import AddToWishListView, RemoveFromWishListView, UsersWishList


router = routers.DefaultRouter()
router.register(r'wishlist', UsersWishList, basename='wishlist')

app_name = 'product'

urlpatterns = [path('add-product/<int:pk>', AddToWishListView.as_view(),
                    name='add-product'),
               path('remove-product/<int:pk>', RemoveFromWishListView.as_view(),
                    name='remove-product'),
               path('list/', include(router.urls))

               ]
