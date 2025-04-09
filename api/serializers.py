from api.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'photo', 'created_at', 'updated_at']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['url', 'email', 'subject', 'message', 'sent_at', 'created_at']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['url', 'name', 'description', 'created_at', 'updated_at']
