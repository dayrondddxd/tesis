from rest_framework import serializers
from .models import Integration

class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        # fields = ('userid', 'username','password','firstname','lastname','email')
        fields = "__all__"



        