from django.urls import path, include

urlpatterns = [
    path('galleries/', include('galleries.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls')),
    path('testimonials/', include('testimonials.urls')),

]
