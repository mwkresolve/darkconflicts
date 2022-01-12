from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import Log, Processes
from datetime import timedelta, date, datetime

class LogPageView(TemplateView):
    template_name = "log.html"

    def get(self, request):
        my_log = Log.objects.filter(userid=request.user).values()
        for a in my_log:
            log = dict(a)['text']
            return render(request, self.template_name, {'mylog': log})
    def post(self, request):
        endtime = datetime.now() + timedelta(seconds=10)
        current_log = request.POST.get('logarea')
        Processes.objects.create(userid=request.user,
                                action=1,
                                timestart=datetime.now(),
                                timeend=endtime, logedit=current_log)
        return HttpResponseRedirect("/task/")
