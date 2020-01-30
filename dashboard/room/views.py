from django.shortcuts import render
from django.views.generic import ListView
from api.models import Room, Building
from dashboard.views import BaseIndexView
from django.db.models import Count

class RoomIndexView(BaseIndexView):
    model = Room
    template_name = "room/list.html"
    filter_by = 'building__furnitures__name'
    filter_tag= 'number'

    def get_context_data(self, *args, **kwargs):
        context = super(RoomIndexView, self).get_context_data(*args, **kwargs)
        total={}
        objs = context['object_list'][0]
        obj_tags = context['object_list'][1]
        for obj_tag in obj_tags:
            amount = objs.filter(number=obj_tag[0]).aggregate(total=Count(self.filter_by))
            total[obj_tag[0]] = amount.get('total')
        context['totals'] =total
        context['object_list'] = objs
        return context
