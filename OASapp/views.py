from django.shortcuts import render
from .forms import UserTextForm
from .models import AcroText
from django.http import HttpResponse
import json


def index(request):
    if request.method == "POST":
        user_text = request.POST.get('Input_text')
        print(user_text)
        response_data = user_text
        return HttpResponse(response_data)
    else:
        return render(request, "main.html", {"form_text": UserTextForm()})



