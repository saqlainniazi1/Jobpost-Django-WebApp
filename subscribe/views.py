from django.shortcuts import render, redirect
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe


# Create your views here.

def subscribe(request):

    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():

            subscribe_form.save()

            # print("is valid")
            # data = subscribe_form.cleaned_data
            # first_name = data['first_name']
            # last_name = data['last_name']
            # email = data['email']
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))

    context = {
        "email_error_empty": email_error_empty,
        "form": subscribe_form
    }
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):

    context = {}
    return render(request, 'subscribe/thank_you.html', context)
