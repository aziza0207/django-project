from django.urls import path
from .views import CreateUserView, CreateTokenView, ManageUserView

app_name = 'user'

urlpatterns = [path('register/', CreateUserView.as_view(), name='register'),
               path('token/', CreateTokenView.as_view(), name='token'),
               path('user-detail/', ManageUserView.as_view(), name='user-detail')]
