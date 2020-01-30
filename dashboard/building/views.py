from django.shortcuts import render
from api.models import Building
from django.views.generic import ListView

class BuildingIndexView(ListView):
    model = Building
    template_name = "building/list.html"

    def get_context_data(self):
        context = super(BuildingIndexView, self).get_context_data()
        buildings = context['building_list']
        building_names = buildings.values_list('name').distinct()
        total ={}
        for building_name in building_names:
            amount = buildings.filter(name=building_name[0]).values_list(
            'rooms__areas__furnitures__name').count()
            total[building_name[0]] = amount
        context['totals'] =total
        return context
