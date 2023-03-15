from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('booking/',views.BookingViewSet.as_view({'get':'list','post':'create'})),
    path('menu-items/', views.MenuView.as_view({'get': "list", "post": "create"})),
    path('menu-items/<int:pk>', views.MenuView.as_view({'get':'retrieve','delete':'destroy'})),
    path('users/',views.UserViewSet.as_view({'get':'list'})),
]
