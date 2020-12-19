from django.urls import path

from . import views


urlpatterns = [
  # ex: /polls/
  path("", views.index, name="index"),
  # ex: /polls/5/
  path("<int:quest_id>/", views.detail, name="details"),
  # ex: /polls/5/results/
  path("<int:quest_id>/results/", views.results, name="results"),
  # ex: /polls/5/vote/
  path("<int:quest_id>/vote/", views.vote, name="vote")
]
