from django.shortcuts import render
from django.views.generic import ListView
from api.models import Area


class AreaIndexView(ListView):
    model = Area
    template_name = "area/list.html"

    def get_context_data(self):
        context = super(AreaIndexView, self).get_context_data()
        areas = context['area_list']
        area_names = areas.values_list('name').distinct()
        total ={}
        for area_name in area_names:
            amount = areas.filter(name=area_name[0]).values_list(
            'furnitures__name').count()
            total[area_name[0]] = amount
        context['totals'] =total
        return context
