from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from baking_app.models import Bake, Category


class IndexView(generic.ListView):
    template_name = 'bakes/index.html'
    context_object_name = 'bakes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        name = self.request.GET.get('name')
        category = self.request.GET.get('category')
        bakes = Bake.objects.all()
        if category:
            bakes = bakes.filter(category__id=category)
        if name:
            bakes = bakes.filter(title__icontains=name)
        return bakes.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_count'] = len(context['categories'])
        context['successes_count'] = context['bakes_list'].filter(success=True).count()
        context['failures_count'] = context['bakes_list'].filter(success=False).count()
        return context


class DetailView(generic.DetailView):
    model = Bake
    template_name = 'bakes/detail.html'
