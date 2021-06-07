import uuid
from django.urls import path

from .views import ServiceList, ServiceRetrieve

urlpatterns = [
    path('<uuid:pk>/', ServiceRetrieve.as_view()),
    path('', ServiceList.as_view())
]
