from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterationNewuser
from .serializer import UserSerializer
from .tasks import send_email


class SendMailView(generics.GenericAPIView):
    def post(self, request):
        data = request.data
        send_email.delay(data)
        return Response("The Email has been sent.", status=status.HTTP_200_OK)

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = RegisterationNewuser.objects.all()