from django.urls import path

from .views import GalleryListCreateAPIView, GalleryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', GalleryRetrieveUpdateDestroyAPIView.as_view()),
    path('', GalleryListCreateAPIView.as_view())
]
