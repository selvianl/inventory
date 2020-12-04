from rest_framework import serializers
from api.models import *
from rest_framework import exceptions

class FurnitureSerializer(serializers.ModelSerializer):
    """
    Bu boktan bir serialierdir
    Modeldeki butun fieldlari kabul eder.
    """

    def validate(self, data):
        furniture, _ = Furniture.objects.get_or_create(**data)
        return furniture

    def save(self):
        return self.validated_data

    class Meta:
        model=Furniture
        fields = ("id", "name", "price")


class FurnitureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Furniture
        fields = ("id", "name", "price")


class AreaSerializer(serializers.ModelSerializer):

    def validate(self, data):
        area, _ = Area.objects.get_or_create(**data)
        return area

    def save(self):
        return self.validated_data

    class Meta:
        model=Area
        fields = ("id", "name")


class AreaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields = ("id", "name")


class RoomSerializer(serializers.ModelSerializer):

    def validate(self, data):
        room, _ = Room.objects.get_or_create(**data)
        return room

    def save(self):
        return self.validated_data

    class Meta:
        model=Room
        fields = ("id", "number")


class RoomUpdateSerializer(serializers.ModelSerializer):
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
        building = Building.objects.create(name=validated_data['name'])
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
        import ipdb
        ipdb.set_trace()
        name = validated_data['name']
        for furniture in validated_data['furnitures']:
            instance.furnitures.clear()
            instance.furnitures.add(furniture)
        for room in validated_data['rooms']:
            instance.rooms.clear()
            instance.rooms.add(room)
        for area in validated_data['areas']:
            instance.areas.clear()
            instance.areas.add(area)
        instance.name = name
        instance.save()
        return instance
