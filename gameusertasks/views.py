from django.http import HttpResponseRedirect
from django.shortcuts import render
from controller.models import Processes, Log, Software, User, HackedDatabase
from django.db.models import Max
from django.shortcuts import redirect
from gameinternet.views import hackip


def TasksView(request):
    print('chegou tasks')
    tasks = Processes.objects.filter(userid=request.user).values()
    tasks_not_complet = Processes.objects.filter(userid=request.user, completed=False).values()

    return render(request, "tasks.html", {'tasks': tasks, 'sem_task': len(tasks_not_complet)})




def CompleteTask(request):
    get_id = request.get_full_path().split('%3D')[1]
    task = Processes.objects.filter(userid=request.user, id=get_id).values()
    # garantir que somente vai manipular as proprias tasks
    if len(task) > 0:
        # garantir que nao vai rodar processo ja concluido
        for infos in task:
            if not infos['completed']:
                if infos['action'] == 1: # action editar log
                    print('acao de editar log')
                    Log.objects.filter(userid=request.user).update(text=infos['logedit'])
                    Processes.objects.filter(userid=request.user, id=get_id).update(completed=True)
                    return HttpResponseRedirect("log/")
                if infos['action'] == 2:  # tentar hackear ip
                    ip_victim = infos['iptryhack']
                    softs_user = Software.objects.filter(userid=request.user, softtype_id=1).values()
                    maxlvl_crc_user = softs_user.aggregate(Max('softversion'))['softversion__max']
                    victim = User.objects.filter(gameip=ip_victim).values_list('id')[0][0]
                    softs_victim = Software.objects.filter(userid=victim, softtype_id=2).values_list()
                    maxlvl_hash_victim = softs_victim.aggregate(Max('softversion'))['softversion__max']
                    if not maxlvl_hash_victim:
                        maxlvl_hash_victim = 0
                    if maxlvl_crc_user >= maxlvl_hash_victim:
                        HackedDatabase.objects.create(userid=request.user, iphacked=ip_victim)
                        Processes.objects.filter(userid=request.user, id=get_id).update(completed=True)
                        msgbroke = """<span style="color: green"> Você conseguiu hackear o servidor</span>"""
                        return hackip(request, msgbroke, ip_victim)
                    else:
                        Processes.objects.filter(userid=request.user, id=get_id).update(completed=True)
                        msgbroke = """<span style="color: red"> Seu cracker não é bom o suficiente</span>"""
                        return hackip(request, msgbroke, ip_victim)
    else:
        print('esse processo  não é seu')

    return render(request, "tasks.html")
