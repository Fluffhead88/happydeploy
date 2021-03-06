from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import Timestamp
from rest_framework import generics
from app.serializers import TimestampSerializer


class IndexView(TemplateView):
    template_name = "index.html"


class TimestampListCreateAPIView(generics.ListCreateAPIView):
    queryset = Timestamp.objects.all()
    serializer_class = TimestampSerializer
