from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.views.generic import ListView
from django.db.models import Q

class SearchResultsView(ListView):
    model = Product
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(name__contains=query) | Q(description__contains=query))
        return object_list