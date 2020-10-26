from django.urls import path, include
from api import views
from rest_auth.views import LoginView,LogoutView
from rest_auth.registration.views import RegisterView

urlpatterns = [
    path('login', LoginView().as_view(),
         name="login"),
    path('logout', LogoutView().as_view(),
         name="logout"),
    path('register', RegisterView().as_view(),
         name="register"),
    path('furnitures/', views.FurnitureView.as_view(),
        name='furnitures'),
    path('furnitures/<int:id>/', views.FurnitureUpdateView.as_view(),
        name='furniture_update'),
    path('areas/', views.AreaView.as_view(),
        name='areas'),
    path('areas/<int:id>/', views.AreaUpdateView.as_view(),
        name='area_update'),
    path('rooms/', views.RoomView.as_view(),
        name='rooms'),
    path('rooms/<int:id>/', views.RoomUpdateView.as_view(),
        name='room_update'),
    path('buildings/', views.BuildingView.as_view(),
        name='buildings'),
    path('buildings/<int:id>/', views.BuildingUpdateView.as_view(),
        name='building_update'),
]
