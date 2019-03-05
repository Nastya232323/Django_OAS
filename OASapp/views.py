from django.shortcuts import render
from .forms import UserTextForm
from .models import AcroText
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

acrotext = AcroText()


def index(request):
    return render(request, "main.html", {"form_text": UserTextForm()})


@csrf_exempt
def ajax_get(request):
    user_text = request.POST.get('Input_text')
    acrotext.set_text(user_text)
    acrotext.do_word("")
    response_data = json.dumps({"words": acrotext.get_top_words()})
    return HttpResponse(response_data)


@csrf_exempt
def ajax_words(request):
    new_word = request.POST.get('word')
    message = acrotext.do_word(new_word)
    response_data = json.dumps({"words": acrotext.get_top_words(),
                                "message": message})
    return HttpResponse(response_data)