from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faqs')

urlpatterns = router.urls