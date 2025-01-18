"""
URL mappings for the user API.
"""
from django.urls import path
from user.views import CreateUserView, ObtainAuthToken


app_name = 'user'


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', ObtainAuthToken.as_view(), name='token'), 
]
