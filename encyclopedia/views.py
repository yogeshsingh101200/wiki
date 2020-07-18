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
