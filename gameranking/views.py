from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import *

class RankingPageView(TemplateView):

    template_name = "ranking.html"

    def get(self, request):
        rank = dict()
        rankusr = HistUsersCurrent.objects.order_by('-reputation')
        return render(request, self.template_name, {'context': rankusr})
