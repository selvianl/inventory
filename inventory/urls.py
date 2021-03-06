"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf  import settings

from dashboard.views import index
urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include('api.urls')),
    path('dashboard/', include(('dashboard.building.urls', 'dashboard.building'), namespace="building")),
    path('dashboard/', include(('dashboard.area.urls', 'dashboard.area'), namespace="area")),
    path('dashboard/', include(('dashboard.furniture.urls', 'dashboard.furniture'), namespace="furniture")),
    path('dashboard/', include(('dashboard.room.urls', 'dashboard.room'), namespace="room")),

]
