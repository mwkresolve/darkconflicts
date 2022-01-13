import re
from datetime import timedelta, date, datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import User, Processes, Software, TypeSofts, HackedDatabase


def GenerateIpUrl():
    get_ips = User.objects.values('gameip')
    all_ips_game = list()
    for ip in get_ips.iterator():
        all_ips_game.append(ip['gameip'])
    return all_ips_game

def disconnectuser(request):
    info_user = User.objects.filter(username=request.user).values()
    ip_connect = info_user[0]['ipconnected']
    if ip_connect == 'off':
        return HttpResponseRedirect("/internet/")
    else:
        User.objects.update(ipconnected='off')
        return HttpResponseRedirect("/internet/")


def IpConnectView(request):
    info_user = User.objects.filter(username=request.user).values()
    ip_connect = info_user[0]['ipconnected']
    if ip_connect == 'off':
        return HttpResponseRedirect("/internet/")
    victim = User.objects.filter(gameip=ip_connect).values('log', 'username', 'id')
    softs_victim = Software.objects.filter(userid=victim[0]['id']).values()

    return render(request, "internet_connect_ip_ok.html", {'softs_victim':softs_victim})

def hackip(request, msgbroke, ip_victim):
    info_victim = User.objects.filter(gameip=ip_victim).values('isnpc', 'username', 'gamepass')
    for info in info_victim:
        if info['isnpc']:
            text_npc = f'Olá invasor, meu nome é {info["username"]}.</br> quem sabe eu possa te ajudar se você me responder uma pergunta ' \
                       f'\nMas espera ai, sera que você consegue me invadir?'
            return render(request, "internethack.html", {'ip_victim': ip_victim,
                                                         'text_npc': text_npc, 'msgbroke':msgbroke})
        else:
            return render(request, "internethack.html", {'msgbroke':msgbroke})


def IpView(request):
    regex_ip = '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
    info_user = User.objects.filter(username=request.user).values()
    ip_victim = re.findall(regex_ip, request.get_full_path())[0]
    ip_connect = info_user[0]['ipconnected']
    if ip_connect != 'off':
        return HttpResponseRedirect(f"/netip={ip_connect}isconnected=ok")
    if request.method == "POST":
        if request.POST.get('action') == 'login':
            user = request.POST.get('user')
            pw = request.POST.get('pass')
            info_victim = User.objects.filter(gameip=ip_victim, gamepass=pw).values()
            if not info_victim:
                # pend retornar na tela que qa senha ta errada
                return HttpResponseRedirect(f"/netip={ip_victim}")
            else:
                User.objects.update(ipconnected=ip_victim)
                return HttpResponseRedirect(f"/netip={ip_victim}isconnected=ok")

        if request.POST.get('tryhack') == 'Try hack':
            hackiptaskactive = len(Processes.objects.filter(userid=request.user, completed=False, iptryhack=ip_victim))
            # usuario só pode ter 1 task ativa para completar
            if hackiptaskactive > 0:
                # criar msg de aviso no front que ja existe uma tarefa em andamento
                return HttpResponseRedirect("/internet/")
            verif_ip_ind_db = len(
                HackedDatabase.objects.filter(userid=request.user, iphacked=ip_victim))
            if verif_ip_ind_db > 0:
                # criar msg de aviso no front que o ip ja esta no banco de dados
                return HttpResponseRedirect("/internet/")
            else:
                endtime = datetime.now() + timedelta(seconds=10)
                Processes.objects.create(userid=request.user,
                                         action=2,
                                         timestart=datetime.now(),
                                         timeend=endtime, iptryhack=ip_victim)
                return HttpResponseRedirect("/task/")
    if ip_victim not in GenerateIpUrl():
        msgerro = f'O IP {ip_victim} não existe'
        return render(request, "internetip.html", {'msgerro': msgerro})
    else:
        # verificar se é npc
        info_victim = User.objects.filter(gameip=ip_victim).values('isnpc', 'username', 'gamepass')
        verif_in_db = len(HackedDatabase.objects.filter(userid=request.user, iphacked=ip_victim))
        pwvictim = ''
        for info in info_victim:
            if verif_in_db > 0:
                pwvictim = info['gamepass']
            if info['isnpc']:
                text_npc = f'Olá invasor, meu nome é {info["username"]}.</br> quem sabe eu possa te ajudar se você me responder uma pergunta ' \
                           f'\nMas espera ai, sera que você consegue me invadir?'

                return render(request, "internethack.html", {'ip_victim': ip_victim,
                                                             'text_npc': text_npc, 'pwvictim': pwvictim} )
            else:
                return render(request, "internethack.html", {'pwvictim': pwvictim})

    return render(request, "internetip.html")



def InternetView(request):
            return HttpResponseRedirect("/netip=0.0.0.0")

