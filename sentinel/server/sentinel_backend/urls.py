from django.contrib import admin
from django.urls import path
from .serializers import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentiment', sentiment_viewset.as_view()),
]
