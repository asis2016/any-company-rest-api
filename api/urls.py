from django.urls import path, include

urlpatterns = [
    # services
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls'))

]
