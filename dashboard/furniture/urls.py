from django.urls import path, include
from dashboard.furniture import views

urlpatterns = [

    path('furnitures/', views.FurnitureIndexView.as_view(),
        name='index'),

]
