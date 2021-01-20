from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from application.models import Dojo, Ninjas

# Create your views here.


def index(request):
    context = {
        'all_dojos':Dojo.objects.all(),
        'all_ninjas': Ninjas.objects.all()
    }
    return render(request, "index.html", context)


def add_dojo(request):
    name_from_form = request.POST['name']
    city_from_form = request.POST['city']
    state_from_form = request.POST['state']
    Dojo.objects.create(name=name_from_form,
                        city=city_from_form, state=state_from_form)
    return redirect("/")


def add_ninja(request):
    student_name = request.POST['first_name']
    student_last_name = request.POST['last_name']
    dojo_id = request.POST['dojo_list']
    school = Dojo.objects.get(id=dojo_id)
    Ninjas.objects.create(
        first_name = student_name, 
        last_name = student_last_name, 
        dojo = school)
    return redirect("/")
