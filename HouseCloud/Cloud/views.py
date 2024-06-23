from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from Sign.auth_utils import getUser
from HouseCloud.forms import UploadFileForm
from .utils import File, Folder
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
    user = getUser(request)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            # path = f'files/{getUser(request).username}'
            # verificar que el path pertenece al usuario

            path = form.cleaned_data['path']
            father_name = form.cleaned_data['father']
            root_folder = 'files'

            father = Folder(user=user, name=father_name, father=root_folder)
            print(request.FILES['file'])
            new_file = File(
                file=request.FILES['file'], path=path, father=father, user=user)

            os.makedirs(path, exist_ok=True)

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

        elif action == 'request_files':
            """

            - crear objeto folder
            - validar que exista 
            - obtener nombres de archivos de folder

            """

    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})
