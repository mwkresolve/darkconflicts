from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import Log

class LogPageView(TemplateView):
    template_name = "log.html"

    def get(self, request):
        my_log = Log.objects.filter(userid=request.user).values()
        for a in my_log:
            log = dict(a)['text']
            return render(request, self.template_name, {'mylog': log})
    def post(self, request):
        print(request.user)
        current_log = request.POST.get('logarea')
        Log.objects.filter(userid=request.user).update(text=current_log)
        my_log = Log.objects.filter(userid=request.user).values()
        for a in my_log:
            log = dict(a)['text']
            return render(request, self.template_name, {'mylog': log})