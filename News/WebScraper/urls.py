from django.urls import path
from .views import NewsView

app_name = "WebScraper"

urlpatterns = [

    path('news/', NewsView.as_view(),
    name="news-list"),
]