from django.urls import path

from .views import TestimonialListCreateAPIView, TestimonialRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', TestimonialRetrieveUpdateDestroyAPIView.as_view()),
    path('', TestimonialListCreateAPIView.as_view())
]
