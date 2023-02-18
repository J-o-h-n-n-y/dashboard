from django.urls import path
from .views import SearchResultView

urlpatterns = [
    path('home', SearchResultView.as_view(), name='home')
]
