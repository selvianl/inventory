from django.shortcuts import render
from api.models import Furniture
from dashboard.views import BaseIndexView
from django.db.models import Count

class FurnitureIndexView(BaseIndexView):
    model = Furniture
    template_name = "furniture/list.html"
    filter_by = 'building__furnitures__name'
    filter_tag = 'name'

    def get_context_data(self, *args, **kwargs):
        context = super(FurnitureIndexView, self).get_context_data(*args, **kwargs)
        total={}
        objs = context['object_list'][0]
        obj_tags = context['object_list'][1]
        for obj_tag in obj_tags:
            amount = objs.filter(name=obj_tag[0]).aggregate(total=Count(self.filter_by))
            total[obj_tag[0]] = amount.get('total')
        context['totals'] =total
        return context
