from django.urls import path
from .views import SendMailView, UserList


app_name = "SendNews"

urlpatterns = [

    path('send-mail/', SendMailView.as_view(),
    name="send-mail"),

    path('list/', UserList.as_view(),
    name="list-user")

]
