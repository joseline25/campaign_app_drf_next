from django.shortcuts import render
from rest_framework import generics
from .models import Campaign, Subscriber

# Create your views here.


# generic views for GET and POST a Subscriber
class CampaignListAPIView(generics.ListAPIView):
    
    def get_queryset(self):
        return super().get_queryset()
        