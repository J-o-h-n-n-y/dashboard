# from django.shortcuts import render
from django.views.generic import ListView

from graphics.models import Budget


class SearchResultView(ListView):
    model = Budget
    template_name = 'home.html'

    def get_queryset(self):
        query = self.request.GET.get('area')        
        year_from = int(self.request.GET.get('year_from'))
        year_to = int(self.request.GET.get('year_to'))
        object_list = Budget.objects.filter(
            year__lte=year_to, 
            year__gte=year_from, 
            area__icontains=query)
        return object_list
