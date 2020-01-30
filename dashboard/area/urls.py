from django.urls import path, include
from dashboard.area import views
urlpatterns = [

    path('areas/', views.AreaIndexView.as_view(),
        name='index'),

]
