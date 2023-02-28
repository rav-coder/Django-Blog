from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Start a python course.",
    "february": "Get everything ready to apply for jobs.",
    "march": "Learn Django in depth.",
    "april": "Learn Django in depth.",
    "may": "Learn Django in depth.",
    "june": "Start a python course.",
    "july": "Learn Django in depth.",
    "august": "Start a python course.",
    "september": None,
    "october": "Learn python in depth.",
    "november": None,
    "december": "Learn Django in depth.",
}


# Create your views here.

def index(request):
    return render(request, "challenges/index.html", {
        "month_list": [month for month in list(monthly_challenges.keys())],
    })


def monthly_challenge_by_num(request, month):
    try:
        forward_month = list(monthly_challenges.keys())[month-1]
    except IndexError:
        return HttpResponseNotFound("This month is not supported!")

    # reverse-engineer to find the path /challenge/january
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
