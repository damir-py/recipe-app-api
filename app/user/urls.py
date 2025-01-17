"""
URL mappings for the user API.
"""
from django.urls import path
from user.views import CreateUserView, CreateTokenView


app_name = 'user'


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
]
