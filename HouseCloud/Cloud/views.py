from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from Sign.auth_utils import getUser
from HouseCloud.forms import UploadFileForm
from .utils import File
import json
import os


@login_required
def index(request):
    """
    This function represents the index view, here the user can upload files.

    Args:
        request (DjangoRequest): The user's request

    Returns:
        JsonResponse: Always contains a 'success': bool element.
        render: Only when the view is accessed
    """

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            path = f'files/{getUser(request).username}'
            os.makedirs(path, exist_ok=True)
            new_file = File(file=request.FILES['file'], path=path)
            save_success = new_file.save()

            response_data = {
                'success': save_success
            }

            return JsonResponse(response_data)

        data = json.loads(request.body)
        action = data['action']

        if action == 'logout':
            logout(request)
            response_data = {
                'success': True
            }
            return JsonResponse(response_data)

    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})
