from rest_framework import routers

from .api import UserViewSet



router = routers.DefaultRouter()

router.register('api/register', UserViewSet, 'register')



urlpatterns = router.urls