from django.urls import path, include
from rest_framework import routers
from .views import ValuesViewset, PrinciplesViewset

router = routers.DefaultRouter()
router.register('values', ValuesViewset)
router.register('principles', PrinciplesViewset)

urlpatterns = [
 path('', include(router.urls)),
]
