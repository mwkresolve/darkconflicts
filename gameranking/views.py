from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import *

class RankingPageView(TemplateView):

    template_name = "ranking.html"

    def get(self, request):
        rankusr = HistUsersCurrent.objects.all()
        print(rankusr)

        return render(request, self.template_name, {'context':rankusr})
