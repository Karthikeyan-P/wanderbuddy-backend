from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView

urlpatterns = [
    path('token/create/', TokenCreateView.as_view(), name='token_create'),
    path('token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),
]
