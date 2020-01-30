from django.db import models


class Furniture(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return u'%s / %s ' % (self.name, self.price)

class Area(models.Model):
    name = models.CharField(max_length=100)
    furnitures = models.ForeignKey(Furniture, on_delete=models.CASCADE)


    def __str__(self):
        return u'%s / %s ' % (self.name, self.furnitures)


class Room(models.Model):
    number = models.PositiveIntegerField()
    areas = models.ForeignKey(Area, on_delete=models.CASCADE)


    def __str__(self):
        return u'%s / %s ' % (self.number, self.areas)


class Building(models.Model):
    name = models.CharField(max_length=25)
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return u'%s / %s ' % (self.name, self.rooms)
