from django.urls import path, include

urlpatterns = [
    path('brands/', include(('brands.urls', 'brands'), namespace='brands')),
    path('galleries/', include(('galleries.urls', 'galleries'), namespace='galleries')),
    path('services/', include(('services.urls', 'services'), namespace='services')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),
    path('testimonials/', include(('testimonials.urls', 'testinominals'), namespace='testinominals')),
]
