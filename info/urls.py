from rest_framework import routers

from .api import InfoViewSet



router = routers.DefaultRouter()

router.register('api/info', InfoViewSet, 'info')



urlpatterns = router.urls 