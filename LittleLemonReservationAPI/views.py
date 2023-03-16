from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ViewSet ,ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .seriailizers import BookingSerializer, MenuSerializer ,UserSerializer
from .models import Booking, Menu
from rest_framework import permissions
from django.contrib.auth.models import User


class MenuView(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request):
        self.permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
        serialized_item = MenuSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]


class Index(TemplateView):
    template_name = "index.html"
