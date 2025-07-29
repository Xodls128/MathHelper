from rest_framework import generics, permissions
from users.models import CustomUser
from users.serializers.user import UserSerializer

class UserMeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
