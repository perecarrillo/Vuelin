from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("gameCreator/", views.gameCreator, name="gameCreator"),
    # ex: /polls/5/results/
    path("waitingRoomHost/", views.waitingRoomHost, name="waitingRoomHost"),
    path("waitingRoomPlayer/", views.waitingRoomPlayer, name="waitingRoomPlayer"),
    path("writePrompt/", views.writePrompt, name="writePrompt"),
    path("playerNameInput/", views.playerNameInput, name="playerNameInput"),
    path("canvas/", views.canvas, name="canvas"),
    path("guessDrawing/", views.guessDrawing, name="guessDrawing"),
]
