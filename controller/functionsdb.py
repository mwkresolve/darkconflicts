from .models import *
import json


def disconnect_ip_victim(user):
    User.objects.filter(username=user).update(ipconnected='off')

def connect_ip_victim(user, ip):
    User.objects.filter(username=user).update(ipconnected=ip)

def create_user_game(user):
    UserStats.objects.create(user=user)
    Hardware.objects.create(userid=user)
    HistUsersCurrent.objects.create(userid=user)
    User.objects.update(stats_game=True)
def creategame():
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

def create_npc_game():
    npc_data = open('my_tools/info_bots.json').read()
    npcList = json.loads(npc_data)
    for bot in npcList:
        name = npcList[bot]['nome']
        gameip = npcList[bot]['ip']
        # create usernpc
        if 'create' in gameip:
            gameip = ip_generator()
        User.objects.create(username=name,
                            isnpc=True,
                            gameip=gameip,
                            gamepass=pwd_generator())
    create_hardware_npc()
    create_softs_npc()

def create_hardware_npc():
    npc_data = open('my_tools/info_bots.json').read()
    npcList = json.loads(npc_data)
    for bot in npcList:
        user = User.objects.get(username=npcList[bot]['nome'])
        cpu = npcList[bot]['cpu']
        hdd = npcList[bot]['hdd']
        ram = npcList[bot]['ram']
        Hardware.objects.create(userid=user, cpu=cpu, hdd=hdd, ram=ram)

def create_softs_npc():
    npc_data = open('my_tools/info_bots.json').read()
    npcList = json.loads(npc_data)
    softsize = 100
    softram = 25
    for bot in npcList:
        user = User.objects.get(username=npcList[bot]['nome'])
        for softs in npcList[bot]['softs']['soft'].values():
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
