from rest_framework import serializers
from .models import *

class content_serializer(serializers.ModelSerializer):
    class Meta:
        model = content_input
        fields = ('content')