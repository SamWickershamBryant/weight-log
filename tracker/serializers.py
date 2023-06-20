from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import WeightEntry

User = get_user_model()
class WeightEntrySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = WeightEntry
        fields = ['user','weight','timestamp']
