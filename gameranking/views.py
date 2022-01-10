from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import User

class RankingPageView(TemplateView):

    template_name = "ranking.html"

    def get(self, request):
        rankusr = User.objects.all()

        return render(request, self.template_name, {'context':rankusr})
