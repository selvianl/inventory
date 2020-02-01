from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from api.models import *
from api.serializers import (FurnitureSerializer, AreaSerializer,
                             RoomSerializer, BuildingSerializer)


class FurnitureView(generics.ListCreateAPIView):
    serializer_class = FurnitureSerializer
    queryset = Furniture.objects.all()


class FurnitureUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FurnitureSerializer
    queryset = Furniture.objects.all()
    lookup_field = 'name'

    def get_object(self):
        return get_object_or_404(Furniture, name=self.kwargs['name'])


class AreaView(generics.ListCreateAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class AreaUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    lookup_field = 'name'

    def get_object(self):
        return get_object_or_404(Area, name=self.kwargs['name'])


class RoomView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'number'

    def get_object(self):
        return get_object_or_404(Room, number=self.kwargs['number'])


class BuildingView(generics.ListCreateAPIView):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()


class BuildingUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(Building, id=self.kwargs['id'])
