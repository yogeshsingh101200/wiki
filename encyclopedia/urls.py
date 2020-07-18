""" Contains url-view mapping for encylopedia app """

from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry")
]
