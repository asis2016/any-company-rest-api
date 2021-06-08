from django.urls import path

from .views import GalleryListCreate, GalleryRetrieveUpdateDestroy

urlpatterns = [
    path('<uuid:pk>/', GalleryRetrieveUpdateDestroy.as_view()),
    path('', GalleryListCreate.as_view())
]
