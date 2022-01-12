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
        if request.method == "POST":
            if request.POST["editlog"]:
                editlogactive = len(Processes.objects.filter(userid=request.user, action=1,completed=False))
                # usuario só pode ter 1 task ativa para completar
                if editlogactive > 0:
                    # criar msg de aviso no front que ja existe uma tarefa em andamento
                    return HttpResponseRedirect("/log/")
                else:
                    endtime = datetime.now() + timedelta(seconds=10)
                    current_log = request.POST.get('logarea')
                    Processes.objects.create(userid=request.user,
                                            action=1,
                                            timestart=datetime.now(),
                                            timeend=endtime, logedit=current_log)
                    return HttpResponseRedirect("/task/")
