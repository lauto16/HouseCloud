from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from Sign.auth_utils import getUser
import json


@login_required
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data['action']

        if action == 'logout':
            logout(request)
            response_data = {
                'success': True
            }
            return JsonResponse(response_data)

    return render(request, 'index.html')
