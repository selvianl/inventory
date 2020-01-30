from django.shortcuts import render
from django.views.generic import ListView
from api.models import Furniture


class FurnitureIndexView(ListView):
    model = Furniture
    template_name = "furniture/list.html"

    def get_context_data(self):
        context = super(FurnitureIndexView, self).get_context_data()
        furnitures = context['furniture_list']
        furniture_names = furnitures.values_list('name').distinct()
        total ={}
        for furniture_name in furniture_names:
            amount = furnitures.filter(name=furniture_name[0]).values_list(
            'name').count()
            total[furniture_name[0]] = amount
        context['totals'] =total
        return context
