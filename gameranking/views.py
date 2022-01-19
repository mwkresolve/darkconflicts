from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import *

class RankingPageView(TemplateView):

    template_name = "ranking.html"

    def get(self, request):
        rank = dict()
        rankusr = HistUsersCurrent.objects.all()
        for c in range(len(rankusr)):
            usr = rankusr[c].userid
            rank = rankusr[c].reputation
            print(usr)
            print(rank)

        return render(request, self.template_name, {'context': rankusr})
