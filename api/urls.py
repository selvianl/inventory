from django.urls import path, include
from api import views

urlpatterns = [
    path('furnitures/', views.FurnitureView.as_view(),
        name='furnitures'),
    path('areas/', views.AreaView.as_view(),
        name='areas'),
    path('rooms/', views.RoomView.as_view(),
        name='rooms'),
    path('buildings/', views.BuildingView.as_view(),
        name='building'),
    path('buildings/<int:id>/', views.BuildingUpdateView.as_view(),
        name='building'),
]
