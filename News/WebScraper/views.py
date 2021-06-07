from rest_framework import generics
from .models import News
from .serializer import NewsSerializer


class NewsView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()