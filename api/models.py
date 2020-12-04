from django.db import models


class Furniture(models.Model):
    """Stores furnitures"""
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return u'%s' % (self.name)


class Area(models.Model):
    """Stores areas"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return u'%s' % (self.name)


class Room(models.Model):
    """Stores rooms"""
    number = models.PositiveIntegerField()

    def __str__(self):
        return u'%s' % (self.number)


class Building(models.Model):
    """Stores buildings"""
    name = models.CharField(max_length=25)
    rooms = models.ManyToManyField(Room)
    areas = models.ManyToManyField(Area)
    furnitures = models.ManyToManyField(Furniture)

    def __str__(self):
        room = " ".join(str(seg) for seg in self.rooms.all())
        area = " ".join(str(seg) for seg in self.areas.all())
        furniture = " ".join(str(seg) for seg in self.furnitures.all())
        return u'%s / %s / %s / %s ' % (self.name, room, area,furniture)
