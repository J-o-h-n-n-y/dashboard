from typing import Any

from django.shortcuts import render

from .models import Budget
from .forms import BudgetForm


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
    if request.method == "POST":
        form = BudgetForm(request.POST, request.FILES)  

        if form.is_valid():
            object_list = Budget.objects.filter(
                region__in=form.cleaned_data.get("region"),
                direction__in=form.cleaned_data.get("direction"),
            )
            return render(request, 'home.html', {"object_list": object_list})
    else:
        form = BudgetForm()
    return render(request, "home.html", {"form": form})
