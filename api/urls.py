from django.urls import path, include
from api import views

urlpatterns = [
    path('furnitures/', views.FurnitureView.as_view(),
        name='furnitures'),
    path('furnitures/<str:name>/', views.FurnitureUpdateView.as_view(),
        name='furniture_update'),
    path('areas/', views.AreaView.as_view(),
        name='areas'),
    path('areas/<str:name>/', views.AreaUpdateView.as_view(),
        name='area_update'),
    path('rooms/', views.RoomView.as_view(),
        name='rooms'),
    path('rooms/<int:number>/', views.RoomUpdateView.as_view(),
        name='room_update'),
    path('buildings/', views.BuildingView.as_view(),
        name='buildings'),
    path('buildings/<int:id>/', views.BuildingUpdateView.as_view(),
        name='building_update'),
]
