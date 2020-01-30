from django.urls import path, include
from dashboard.room import views
urlpatterns = [

    path('rooms/', views.RoomIndexView.as_view(),
        name='index'),

]
