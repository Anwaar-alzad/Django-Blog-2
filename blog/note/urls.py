from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import NoteViewSet


router = SimpleRouter()
router.register('notes', NoteViewSet, basename='note')
urlpatterns = router.urls