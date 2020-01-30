from django.urls import path, include
from dashboard.building import views

urlpatterns = [

    path('buildings/', views.BuildingIndexView.as_view(),
        name='index'),

]
