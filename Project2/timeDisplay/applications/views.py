from django.urls import path
from . import views
from forms import RegistrationForm
# then create an index method:


def index(request):
    form = RegistrationForm()  # We will build this class out in just a minute
    context = {
        # Form is the variable name referencing the instance of our RegistrationForm class
        'myregistrationform': form
    }
    return render(request, 'formtest/index.html', context)
