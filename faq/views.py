from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    cache_key = 'faqs_cache'