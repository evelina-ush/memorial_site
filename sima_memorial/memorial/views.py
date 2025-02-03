from django.http import HttpResponse
from django.shortcuts import render, redirect
from memorial.models import SimaPost

# Create your views here.
def index(request):
    s_post = SimaPost.objects.all()
    return render(request, 'index.html', {'post':s_post[4]} )


def about_page(request):
    return HttpResponse("Будущий раздел <О нас>")


def articles(request, number):
    s_post = SimaPost.objects.all()
    if number == 1:
        sp_post = s_post[0]
        return render(request, 'classic_story.html', {'post': sp_post})
    elif number == 2:
        sp_post = s_post[1]
        return render(request, 'classic_story.html', {'post': sp_post})
    elif number == 3:
        sp_post = s_post[2]
        return render(request, 'classic_story.html', {'post': sp_post})
    elif number == 4:
        sp_post = s_post[3]
        return render(request, 'classic_story.html', {'post': sp_post})
def redirect_to_story_1(request):
    return redirect("/article/1")

def redirect_to_story_2(request):
    return redirect("/article/2")

def redirect_to_story_3(request):
    return redirect("/article/3")

def redirect_to_story_4(request):
    return redirect("/article/4")
def page_not_found(request, exception=404):
    return HttpResponse("<h1>Такой страницы не существует!</h1>")