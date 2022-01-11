from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from controller.views import User


def GenerateIpUrl():
    get_ips = User.objects.values('gameip')
    all_ips_game = list()
    for ip in get_ips.iterator():
        all_ips_game.append(ip['gameip'])
    return all_ips_game



class netView(TemplateView):
    template_name = "baseinternet.html"

    def get(self, request):
        return render(request, self.template_name)



def InternetView(request):
        try:
            ip_victim = request.get_full_path().split('=')[1]
            if ip_victim not in GenerateIpUrl():
                msgerro = f'O IP {ip_victim} não existe'
                return render(request, "internetip.html", {'msgerro':msgerro})
            if ip_victim in GenerateIpUrl():
                # verificar se é npc
                info_victim = User.objects.filter(gameip=ip_victim).values('isnpc', 'username')
                for info in info_victim:
                    if info['isnpc']:
                        text_npc = f'Olá invasor, meu nome é {info["username"]}.</br> quem sabe eu possa te ajudar se você me responder uma pergunta ' \
                                   f'\nMas espera ai, sera que você consegue me invadir?'
                        print(info['username'])
                        return render(request, "internetip.html", {'ip_victim': ip_victim,
                                                                   'text_npc': text_npc})
                    else:
                        return render(request, "internetip.html")


            return render(request, "internetip.html")
        except IndexError:
            msgerro = f'OPS ALGO DEU ERRADO'
            return HttpResponseRedirect("?ip=0.0.0.0")

