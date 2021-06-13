from django.urls import path

from .views import BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view()),
    path('', BrandListCreateAPIView.as_view()),
]
