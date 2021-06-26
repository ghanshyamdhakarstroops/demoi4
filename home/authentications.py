from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect



def logout_required(function):
    def wrapper(request, *args, **kw):
        user=request.user.is_authenticated
        if user:
            logout(request)
            return redirect('home:login')
        else:
            return function(request, *args, **kw)
    return wrapper