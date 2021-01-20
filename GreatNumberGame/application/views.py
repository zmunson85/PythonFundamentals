from django.shortcuts import render, redirect
import random
# _____for num____in order to access the random number module you need to import (from random import) there is a built function (randint)
#  ____for guess ____if you do not include int in the input, by default the input will return a string. In order to convert the string to a number,
# _____we need to pass in the input with int(input_____ this means our http response value= a number, not a string

# Create your views here.


def index(request):
    if not 'number' in request.session:
        request.session['number']=random.randint(1,100)
    return render(request, "index.html")

def check_numbers(request):
    player_num= int(request.POST['number'])
    if request.session['number'] == player_num:
        request.session['text'] = f"{player_num} Correct, Well Done!"
        request.session['color'] = "green"
    elif request.session['number'] > player_num:
        request.session['text'] = "That's too Low "
        request.session['color'] = "red"
    else:
        request.session['text'] = "That's too High"
        request.session['color'] = "red"
    return redirect('/')

def start_again(request):
    request.session.flush()
    return redirect('/')