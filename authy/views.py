#encoding:utf-8

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.shortcuts import render

from forms import LoginForm


def login_user(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                print("The username and password were incorrect.")
    else:
        form = LoginForm()

    context = {
        'form':form,
        'next' : request.GET.get('next', '')
    }

    return render(request, "authy/login.html", context)

