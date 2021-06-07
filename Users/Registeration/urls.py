from django.urls import path
from .views import UserView

app_name = "Registeration"

urlpatterns = [

    path('register/', UserView.as_view(),
    name="registeration"),
]