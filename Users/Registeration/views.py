from rest_framework.response import Response
from rest_framework import generics, status
from .serializer import UserSerializer



class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data["username"]

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"User {username} created successfully.",
            status=status.HTTP_200_OK)
            
        return Response("Registeration Failed.", 
        status=status.HTTP_400_BAD_REQUEST)