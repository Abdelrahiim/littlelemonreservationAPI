from .models import Booking, Menu
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(ModelSerializer):
    last_login = serializers.SerializerMethodField("time_last_login_format")
    date_joined = serializers.SerializerMethodField("time_date_joined_format")

    class Meta:
        model = User
        fields = ['username', 'is_superuser', 'is_staff', "is_active", 'date_joined', "last_login"]

    def time_last_login_format(self, user: User):
        return user.last_login.strftime("%Y-%m-%d %H:%M:%S")

    def time_date_joined_format(self, user: User):
        return user.date_joined.strftime("%Y-%m-%d %H:%M:%S")


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ['id']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
