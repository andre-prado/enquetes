from django.urls import path

from . import views


urlpatterns = [
  # path("teste", views.caminho_teste, name="caminho_teste"),
  path("", views.index, name="index")
]
