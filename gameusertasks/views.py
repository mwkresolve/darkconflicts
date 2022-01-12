from django.http import HttpResponseRedirect
from django.shortcuts import render
from controller.models import Processes, Log


def TasksView(request):
    print('chegou tasks')
    tasks = Processes.objects.filter(userid=request.user).values()
    return render(request, "tasks.html", {'tasks': tasks})


def CompleteTask(request):
    get_id = request.get_full_path().split('%3D')[1]
    task = Processes.objects.filter(userid=request.user, id=get_id).values()
    # garantir que somente vai manipular as proprias tasks
    if len(task) > 0:
        # garantir que nao vai rodar processo ja concluido
        for infos in task:
            if not infos['completed']:
                if infos['action'] == 1:
                    print('acao de editar log')
                    Log.objects.filter(userid=request.user).update(text=infos['logedit'])
                    Processes.objects.filter(userid=request.user, id=get_id).update(completed=True)
                    return HttpResponseRedirect("log/")
    else:
        print('esse processo  não é seu')

    return render(request, "tasks.html")
