""" Contains views for encylopedia app """

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    """ default route """
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
    """ NIL """
    entry_content = util.get_entry(title)
    if entry_content is None:
        raise Http404
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry_content
    })


def create(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        if title in util.list_entries():
            return "already exists"
        content = data.get("content")
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))
    return render(request, "encyclopedia/create.html")


def edit(request, title):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        content = data.get("content")
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))

    content = util.get_entry(title)
    return render(request, "encyclopedia/edit", {
        "title": title,
        "content": content
    })