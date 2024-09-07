from django.shortcuts import render
import requests

API_KEY = "aa29f0bbe4a6457b8d224412ae53631a"


def get_articles(category="all", lang="ru", pageSize=100):
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={category}&language={lang}&pageSize={pageSize}&apiKey={API_KEY}"
    )
    data = response.json()
    if data["status"] != "ok":
        print("[!] Ошибка в получении новостей")
        return
    return data["articles"]


def homepage_view(request):
    news = get_articles(category="Minecraft", pageSize=10)
    return render(request, "index.html", {"news": news})


# TO-DO: создать страницу about.html
def favourite(request): ...