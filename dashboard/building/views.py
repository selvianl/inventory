from django.shortcuts import render
from api.models import Building
from django.views.generic import ListView
from dashboard.views import BaseIndexView
from django.db.models import Count


class BuildingIndexView(BaseIndexView):
    model = Building
    filter_tag = 'name'
    template_name = "building/list.html"
    filter_by = 'furnitures__name'


    def get_context_data(self, *args, **kwargs):
        context = super(BuildingIndexView, self).get_context_data(*args, **kwargs)
        total={}
        objs = context['object_list'][0]
        obj_tags = context['object_list'][1]
        for obj_tag in obj_tags:
            amount = objs.filter(name=obj_tag[0]).aggregate(total=Count(self.filter_by))
            total[obj_tag[0]] = amount.get('total')
        context['totals'] =total
        context['object_list'] = objs
        return context
