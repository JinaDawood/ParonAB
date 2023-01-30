from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib import messages

from paron.decorators import unauthenticated_user, allowed_user
from paron.models import Balance, Product
from paron.forms import DeliveryForm


# Create your views here.

@unauthenticated_user
def home_view(request):
    # retrieve form through http post request
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # check if the form is valid and authenticate user with password and username
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # if user exists call login function and redirect to player view
            if user is not None:
                login(request, user)
                if user.groups.filter(name='supervisor').exists():
                    return redirect('manager')
                elif user.groups.filter(name='staff').exists():
                    return redirect('staff')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "Home.html", context={'login_form': form})


@login_required
@allowed_user(allowed_roles=['supervisor'])
def manager_view(request):
    balances = Balance.objects.all()
    return render(request, "Manager.html", context={ 'balances':balances})


@login_required
@allowed_user(allowed_roles=['staff'])
def staff_view(request):
    # call the form to create users
    delivery_form = DeliveryForm()
    # retrieve form values through http post request
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        if delivery_form.is_valid():  # check if it's valid
            # save user using form values and lower case the username string
            delivery = delivery_form.save(commit=False)
            delivery.type = delivery.type.lower()
            delivery.save()
            messages.success(request, "Delivery successful.")
        else:
            # reset the form if the form is not valid and show message to user
            messages.error(request, "Unsuccessful Delivery report. Invalid information.")
            delivery_form = DeliveryForm()
            # pass the form to the html view as context
    context = {'delivery_form': delivery_form}
    return render(request, "Staff.html", context)


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')
