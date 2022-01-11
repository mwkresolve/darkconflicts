"""darkconflicts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from controller.views import Controller, HomePageView
from django.contrib.auth.decorators import login_required
from gameranking.views import RankingPageView
from gamelogfile.views import LogPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("gamesoftware.urls")),
    path("", include("gamehardware.urls")),
    path("", include("gameinternet.urls")),
    path("accounts/", include("allauth.urls")),
    path("log/", LogPageView.as_view(), name="gamelogfile"),
    path("ranking/", RankingPageView.as_view(), name="gameranking"),
    path('admin/', admin.site.urls),
    path('controller/', login_required(Controller.as_view()), name='controller'),
    path('', login_required(HomePageView), name='home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
