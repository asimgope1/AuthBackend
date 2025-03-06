from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Auth Backend 🚀"})

urlpatterns = [
    path('', home, name='home'),  # Default Home Route
    path('admin/', admin.site.urls),
    path('api/auth/', include('authapi.urls')),  # Include app URLs
]
