from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string









monthly_challenges={
    "january": "Let's begin the show",
    "february": "The show still on",
    "march":"Y'all should enjoy the show",
    "april": "Wrapping up the show",
    "may":"Getting to the end of the show",
    "june":"That's it coming!!!",
    "july":"End of the show",
    "august":None,
    "semptember":None,
    "october":None,
    "november":None,
    "December":None
}



def homepage(request):

    
    months = list(monthly_challenges.keys())

    return render(request,"feature/index.html",{
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args= [redirect_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        
        return render(request,"feature/feature.html",{
            "text": challenge_text,
            "month_name":month 

        })
    except:
        return HttpResponseNotFound("UNSUPPORTED MONTH")