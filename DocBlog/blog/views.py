from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



# Create your views here.
def index(request):
    date = datetime.today()
    return render(request, "blog/index.html", context={"date": date})

def article(request, numero_article):
    if numero_article in ["01","02","03"]:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, f"blog/article_not_found.html")