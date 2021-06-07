from django.urls import path

from services.views import ServiceAPIView

urlpatterns = [
    path('', ServiceAPIView.as_view())
]
