from rest_framework.routers import SimpleRouter

from .views import ProjectViewset

router = SimpleRouter()
router.register('', ProjectViewset, basename='projects')
urlpatterns = router.urls

# from .views import ProjectList, ProjectDetail

# urlpatterns = [
# path('<uuid:pk>/', ProjectDetail.as_view()),
# path('', ProjectList.as_view())
# ]
