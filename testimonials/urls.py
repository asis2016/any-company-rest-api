from django.urls import path

from .views import TestimonialListCreate, TestimonialRetrieve

urlpatterns = [
    path('<uuid:pk>/', TestimonialRetrieve.as_view()),
    path('', TestimonialListCreate.as_view())
]
