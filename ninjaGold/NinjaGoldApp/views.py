from django.shortcuts import render, redirect
from time import gmtime, strftime
import random
# Create your views here.


def index(request):
    if not 'your_gold' in request.session:
        request.session['your_gold'] = 0
    if not 'my_list' in request.session:
        request.session['my_list'] = []
    return render(request, "index.html")


def process(request):
    random_for_farm = random.randint(10, 20)
    random_for_cave = random.randint(5, 10)
    random_for_house = random.randint(2, 5)
    random_for_casino = random.randint(-50, 50)
    location = request.POST['location']
    date = strftime("%b %d, %Y", gmtime())
    time = strftime("%I:%M %p", gmtime())
    if location == 'farm':
        request.session['your_gold'] += random_for_farm
        message = f"Earned {random_for_farm} golds from the farm {date} {time}"
        request.session['my_list'].append(message)
    elif location == 'cave':
        request.session['your_gold'] += random_for_cave
        message = f"Earned {random_for_cave} golds from the cave {date} {time}"
        request.session['my_list'].append(message)
    elif location == 'house':
        request.session['your_gold'] += random_for_house
        message = f"Earned {random_for_house} golds from the house {date} {time}"
        request.session['my_list'].append(message)
    elif location == 'casino':
        if random_for_casino > 0:
            request.session['your_gold'] += random_for_casino
            message = f"Earned {random_for_casino} golds from the casino {date} {time}"
            request.session['my_list'].append(message)
        else:
            request.session['your_gold'] += random_for_casino
            positive_number_display = random_for_casino * -1
            message = f"Entered a casino and lost {positive_number_display} golds .... Ouch.. {date} {time}"
            request.session['my_list'].append(message)
    return redirect("/")


def restart(request):
    request.session.flush()
    return redirect('/')
