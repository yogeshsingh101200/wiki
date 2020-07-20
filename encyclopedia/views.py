""" Contains views for encylopedia app """

import random

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from markdown2 import markdown

from . import util


def index(request):
    """ Main route """
    if request.method == "POST":
        form_data = request.POST
        query = form_data.get("q")
        entries = util.list_entries()
        similar = []
        for a_entry in entries:
            if query == a_entry:
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=(a_entry,)))
            if query in a_entry:
                similar.append(a_entry)
        return render(request, "encyclopedia/index.html", {
            "entries": similar
        })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    """ Displays the requested entry """
    entry_content = util.get_entry(title)
    if entry_content is None:
        raise Http404
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": markdown(entry_content)
    })


def create(request):
    """ Creates the entry """
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "error": "Entry already exists!"
            })
        content = data.get("content")
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))
    return render(request, "encyclopedia/create.html")


def edit(request, title):
    """ Edits the entry """
    if request.method == "POST":
        data = request.POST
        content = data.get("content")
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))

    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def randompage(request):
    """ Renders random page from entries """
    try:
        raise IndexError
        title = random.choice(util.list_entries())
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))
    except IndexError:
        return render(request, "encyclopedia/error.html", {
            "error": markdown(f"No page exists!\n[Create]({reverse('encyclopedia:create')})")
        })


def handler404(request, exception):
    return HttpResponseNotFound(render(request, "encyclopedia/error.html", {
        "error": "Page not found"
    }))
