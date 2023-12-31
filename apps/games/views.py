# Django
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet

# Local
from .models import Game, Company


def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/index.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

def games(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/video.html'
    queryset: QuerySet[Game] = Game.objects.all()
    return render(
        request=request,
        template_name=template_name,
        context={
            'games': queryset
        }
    )

def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/about.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

def get_game(request: HttpRequest, game_id: int) -> HttpResponse:
    try:
        game: Game = Game.objects.get(id=game_id)
        queryset: QuerySet[Game] = Game.objects.all() 
        template_name: str = 'games/games.html'
    except Game.DoesNotExist as e:
        return HttpResponse(
            f'<h1>Игры с id {game_id} не существует!</h1>'
            )
    return render(
        request=request,
        template_name=template_name,
        context={
            'games': game,
            'genre': queryset
        }
    )


def get_company(request: HttpRequest, game_id: int, company_id: int) -> HttpResponse:
    try:
        game: Game = Game.objects.get(pk=game_id)
        company: Company = Company.objects.get(id=game.company_id)
        template_name: str = 'games/company.html'
    except Game.DoesNotExist as e:
        return HttpResponse(f'<h1>Игры с id {game_id} не существует!</h1>')
    return render(
        request=request,
        template_name=template_name,
        context={
            'company': company
        }
    )