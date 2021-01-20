from django.shortcuts import render, redirect
from tvShowsApp.models import Show
from django.contrib import messages

# Create your views here.
from . models import Show


def index(request):
    return redirect("/shows")


def all_shows(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request, "all_shows.html", context)


def add_show_template(request):
    return render(request, "add_show.html")


def create_show(request):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')

    else:

        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            date=request.POST['date'],
            desc=request.POST['description'],
        )
        newShow = Show.objects.last()
        showId = newShow.id
        return redirect(f'/shows/{showId}')


def show_info_template(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        "show": show
    }
    return render(request, "show_info.html", context)


def edit_info_from_info_template(request, show_id):
    return redirect(f"/shows/{show_id}/update")


def update_info_template(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, "edit_show.html", context)


def update_info(request, show_id):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{show_id}/update')

    
    show_update = Show.objects.get(id=show_id)
    show_update.title = request.POST['title']
    show_update.network = request.POST['network']
    show_update.desc = request.POST['date']
    show_update.desc = request.POST['description']
    show_update.save()
    return redirect(f"/shows/{show_id}")


def delete_show(request, show_id):
    show_deleted = Show.objects.get(id=show_id)
    show_deleted.delete()
    return redirect("/shows")
