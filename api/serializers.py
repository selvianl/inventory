from rest_framework import serializers
from api.models import *
from rest_framework import exceptions

class FurnitureSerializer(serializers.ModelSerializer):

    class Meta:
        model=Furniture
        fields = ("id", "name", "price")


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Area
        fields = ("id", "name")


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model=Room
        fields = ("id", "number")


class BuildingSerializer(serializers.ModelSerializer):
    furnitures = FurnitureSerializer(many=True)
    areas = AreaSerializer(many=True)
    rooms = RoomSerializer(many=True)

    class Meta:
        model=Building
        fields = ('id', 'name', 'furnitures', 'areas', 'rooms')


    def create(self, validated_data):
        building, _  = Building.objects.get_or_create(name=validated_data['name'])
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
        name = validated_data['name']
        for furniture in validated_data['furnitures']:
            furniture_obj, _ = Furniture.objects.get_or_create(**furniture)
            instance.furnitures.clear()
            instance.furnitures.add(furniture_obj)
        for room in validated_data['rooms']:
            room_obj, _ = Room.objects.get_or_create(**room)
            instance.rooms.clear()
            instance.rooms.add(room_obj)
        for area in validated_data['areas']:
            area_obj, _ = Area.objects.get_or_create(**area)
            instance.areas.clear()
            instance.areas.add(area_obj)
        instance.name = name
        instance.save()
        return instance
