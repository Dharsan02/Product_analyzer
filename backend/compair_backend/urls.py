from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "PriceWise Backend is Running!",
        "status": "success"
    })

urlpatterns = [
    path("", home),   # <-- Add this line

    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/", include("products.urls")),
]