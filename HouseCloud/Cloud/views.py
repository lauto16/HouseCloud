from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Sign.auth_utils import getUser


@login_required
def index(request):
    return render(request, 'index.html')
