from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
