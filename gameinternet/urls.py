from django.urls import path
from .views import InternetView, GenerateIpUrl
app_name = "gameinternet"

urlsips = []
for ip in GenerateIpUrl():
    urlsips.append(path(f"internet?ip={ip}", InternetView, name="internet")),



urlpatterns = urlsips + [

    path("internet/", InternetView, name="gameinternet"),
]
