from django.shortcuts import render
from .forms import UserTextForm
from .models import AcroText
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "main.html", {"form_text": UserTextForm()})


@csrf_exempt
def ajax(request):
    user_text = request.POST.get('Input_text')
    acrotext = AcroText(user_text)
    response_data = json.dumps({"text": acrotext.get_acrotext(),
                                "words": acrotext.get_top_words()})
    return HttpResponse(response_data)
