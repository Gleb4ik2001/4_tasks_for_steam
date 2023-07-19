from django.urls import path

# Local
from .views import index, about, get_game, games, get_company


urlpatterns = [
    path('', index),
    path('about/', about),
    path('list/<int:game_id>/', get_game),
    path('list/', games),
    path('list/<int:game_id>/<int:company_id>/', get_company),
]
