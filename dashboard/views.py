from django.shortcuts import render
from django.views.generic import ListView

class BaseIndexView(ListView):
    model = None
    template_name = None
    filter_by = None
    filter_tag = None

    def get_queryset(self):
        qs = super(BaseIndexView, self).get_queryset()
        qs_tags = qs.values_list(self.filter_tag).distinct()
        return qs, qs_tags


def index(request):
    return render(request, 'index.html')
