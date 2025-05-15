from rest_framework import serializers
from .models import Integration
from .models import MoodleQuizAttempt

class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        # fields = ('userid', 'username','password','firstname','lastname','email')
        fields = "__all__"



class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodleQuizAttempt
        fields = ['id', 'quiz', 'userid', 'state', 'sumgrades', 'timefinish']