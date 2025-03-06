from django.urls import path
from .views import RegisterView, LoginView
from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Welcome to Auth Backend"})

urlpatterns = [
    path('', home),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
