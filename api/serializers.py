from rest_framework import serializers
from api.models import *
from rest_framework import exceptions

class FurnitureSerializer(serializers.ModelSerializer):

    class Meta:
        model=Furniture
        fields = ("name", "price")


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Area
        fields = ("name",)


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model=Room
        fields = ("number",)


class BuildingSerializer(serializers.ModelSerializer):
    furnitures = FurnitureSerializer(many=True, read_only=True)
    areas = AreaSerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model=Building
        fields = ('name', 'furnitures', 'areas', 'rooms')

    def create(self, validated_data):
        building = Building.objects.create(**validated_data)
        for furniture in self.initial_data.pop('furnitures'):
            furniture_obj, _ = Furniture.objects.get_or_create(**furniture)
            building.furnitures.add(furniture_obj)
        for room in self.initial_data.pop('rooms'):
            room_obj, _ = Room.objects.get_or_create(**room)
            building.rooms.add(room_obj)
        for area in self.initial_data.pop('areas'):
            area_obj, _ = Area.objects.get_or_create(**area)
            building.areas.add(area_obj)
        return building

    def update(self, instance, validated_data):
        name = self.validated_data['name']
        furnitures =  self.initial_data['furnitures']
        rooms = self.initial_data['rooms']
        areas = self.initial_data['areas']
        for furniture in furnitures:
            instance.furnitures.clear()
            instance.furnitures.get_or_create(**furniture)
        for room in rooms:
            instance.rooms.clear()
            instance.rooms.get_or_create(**room)
        for area in areas:
            instance.areas.clear()
            instance.areas.get_or_create(**area)
        instance.name = name
        instance.save()
        return instance
