from django.shortcuts import render
from django.views.generic import TemplateView
from controller.models import User, Hardware, TypeSofts, Software, UserStats, Log, HistUsersCurrent
from my_tools.functions import *
import json

def HomePageView(request):
    try:
        if not request.user.stats_game:
            print('criando stats game')
            UserStats.objects.create(user=request.user)
            Log.objects.create(userid=request.user)
            Hardware.objects.create(userid=request.user)
            HistUsersCurrent.objects.create(userid=request.user)
            User.objects.update(stats_game=True)
            print('stats criada')
    except:
        print('jogador não logado')
    return render(request, "home.html")

class Controller(TemplateView):
    template_name = 'controller.html'
    npc_data = open('my_tools/info_bots.json').read()
    npcList = json.loads(npc_data)

    def get(self, request):
        if request.user.is_staff == 1:
            if request.GET.get('createnpc'):
                for bot in self.npcList:
                    name = self.npcList[bot]['nome']
                    gameip = self.npcList[bot]['ip']
                    if 'create' in gameip:
                        gameip = ip_generator()
                    User.objects.create(username=name,
                                        isnpc=True,
                                        gameip=gameip,
                                        gamepass=pwd_generator())
            if request.GET.get('generatehardware'):
                for bot in self.npcList:
                    tempname = self.npcList[bot]['nome']
                    user = User.objects.get(username=tempname)
                    cpu = self.npcList[bot]['cpu']
                    hdd = self.npcList[bot]['hdd']
                    ram = self.npcList[bot]['ram']
                    Hardware.objects.create(userid=user, cpu=cpu, hdd=hdd, ram=ram)

            if request.GET.get('generatetypesofts'):
                Softs_Types = {
                    '1': '.Cracker',
                    '2': '.Hasher',
                    '3': '.PortScan',
                    '4': '.Firewall',
                    '5': '.Hidder',
                    '6': '.Seeker',
                    '7': '.Anti-Virus',
                    '8': '.Spam',
                    '9': '.Warez',
                    '10': '.DDoS',
                    '11': '.Collector',
                    '12': '.Breaker',
                    '13': '.FTPExploit',
                    '14': '.SSHExploit',
                    '15': '.Nmap',
                    '16': '.Analyzer',
                    '17': '.Torrent',
                    '20': '.Miner',
                }
                for soft in Softs_Types:
                    TypeSofts.objects.create(type=Softs_Types[soft])

            if request.GET.get('generatesoftsbots'):
                softsize = 100
                softram = 25
                for bot in self.npcList:
                    user = User.objects.get(username=self.npcList[bot]['nome'])
                    for softs in self.npcList[bot]['softs']['soft'].values():
                        print(user)
                        print(softs['type'])
                        type = TypeSofts.objects.get(type=softs['type'])
                        version = softs['version']
                        softsize = 25
                        softram = 10
                        Software.objects.create(userid=user, softname='s1mple',
                                                softversion=version,
                                                softsize=softsize,
                                                softram=softram,
                                                softtype=type, softhidden=0, softhiddenwith=0)
                    softsize += 100
                    softram += 25
            return render(request, 'controller.html')
        return render(request, 'home.html')