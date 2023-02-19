from typing import Any

from django.shortcuts import render

from .models import Budget
from .forms import SearchForm


# class SearchResultView(ListView):
#     model = Budget
#     template_name = 'home.html'

#     def get_queryset(self, re):
#         regions = self.request.GET.get('region')       
#         direction = self.request.GET.get('direction') 
#         year_from = int(self.request.GET.get('year_from'))
#         year_to = int(self.request.GET.get('year_to'))
#         object_list = Budget.objects.filter(
#             year__lte=year_to, 
#             year__gte=year_from, 
#             region__title=regions,
#             direction__title=direction)
#         return object_list

#     if request.method == "POST":
#         form = TagsForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return HttpResponse("successfully uploaded")
#     else:
#         form = TagsForm()
#     return render(request, "tags/add_tags_form.html", {"form": form})
        
def search(request: Any) -> Any:
    form = SearchForm(request.POST)  
    
    if form.is_valid() and request.method == "POST":
        region_direction = Budget.objects.filter(
            region__title=form.cleaned_data.get("region"),
            direction__title=form.cleaned_data.get("direction"),                
        )
        return render(request, 'home2.html', {"form": form, "region_direction": region_direction})
    else:
        form = SearchForm(request.POST)
    return render(request, "home2.html", {"form": form})
