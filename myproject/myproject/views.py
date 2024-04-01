from rest_framework import generics
from clients.models import Client, Deal
from .serializers import ClientSerializer, DealSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DealList(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class DealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserRegistrationSerializer(user, context=self.get_serializer_context()).data
        }, status=status.HTTP_201_CREATED)