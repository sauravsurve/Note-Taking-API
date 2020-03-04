from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('view',NoteViewSet,basename="note")


urlpatterns = [
   path('article/<int:id>/',include(router.urls)),
   path('article/',include(router.urls)),
]
