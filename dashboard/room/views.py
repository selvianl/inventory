from django.shortcuts import render
from django.views.generic import ListView
from api.models import Room

class RoomIndexView(ListView):
    model = Room
    template_name = "room/list.html"

    def get_context_data(self):
        context = super(RoomIndexView, self).get_context_data()
        rooms = context['room_list']
        room_names = rooms.values_list('number').distinct()
        total ={}
        for room_name in room_names:
            amount = rooms.filter(number=room_name[0]).values_list(
            'areas__furnitures__name').count()
            total[room_name[0]] = amount
        context['totals'] =total
        return context

