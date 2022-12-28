from django.http import JsonResponse
from django.shortcuts import render

from .logic import xml_file_to_json
from .forms import UploadFileForm


def upload_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            json_response = xml_file_to_json(request.FILES['file'])
            return JsonResponse(json_response)
    else:
        form = UploadFileForm()
    return render(request, "upload_page.html", {'form': form})
