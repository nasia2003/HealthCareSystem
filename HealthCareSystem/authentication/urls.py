from django.urls import path
from .views import *

urlpatterns = [
    path('api/register/', RegisterAPI.as_view()),
    path('api/login/', LoginAPI.as_view()),

    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]
