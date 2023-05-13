from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("gameCreator/", views.gameCreator, name="gameCreator"),
    # ex: /polls/5/results/
    path("waitingRoomHost/", views.waitingRoomHost, name="waitingRoomHost"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
