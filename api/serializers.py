from .models import temp_log
from rest_framework import serializers


class tempSerializer(serializers.ModelSerializer):
    class Meta:
        model = temp_log
        fields = '__all__'


CHOICES = (
    ("1", "Broadcast"),
    ("2", "Stop")
)


class broadcast_ser(serializers.Serializer):
    file = serializers.FileField()
    action = serializers.ChoiceField(
        choices=CHOICES)
