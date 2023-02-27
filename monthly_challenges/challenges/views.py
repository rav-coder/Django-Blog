from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start a python course.",
    "february": "Get everything ready to apply for jobs.",
    "march": "Learn Django in depth.",
    "april": "Start a python course.",
    "may": "Learn Django in depth.",
    "june": "Start a python course.",
    "july": "Learn Django in depth.",
    "august": "Start a python course.",
}


# Create your views here.

def index(request):
    response_data = "<ul>"
    for month in monthly_challenges:
        response_data += f"<li><a href={reverse('month-challenge', args=[month])}> {month.capitalize()}</a></li>"
    response_data += "</ul>"
    return HttpResponse(response_data)


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
        challenge_text = monthly_challenges.get(month)
        respone_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    return HttpResponse(respone_data)
