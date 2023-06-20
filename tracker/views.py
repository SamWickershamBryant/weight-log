from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import WeightEntry
from .serializers import WeightEntrySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateWeightEntryView(CreateAPIView):
    model = WeightEntry
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WeightEntrySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WeightEntryListView(ListAPIView):
    serializer_class = WeightEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.META)
        user = self.request.user
        return WeightEntry.objects.filter(user=user)
