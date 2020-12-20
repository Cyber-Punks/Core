from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.core import serializers
from .analyzer import *

class sentiment_viewset(APIView):
    def post(self, request, *args, **kwargs):
        serializer = content_serializer(data = request.data)
        content = serializer.initial_data['content']
        analysis = analyze_entity_sentiment(content)

        return Response(analysis)
        