from django.shortcuts import render
from django.http import HttpResponse

from .helper import multiple_forms, newsletter_form
from .models import FAQ

# Create your views here.


def index(request):
    """ multiple_forms checks if the request  was post, and then depending by the sumit button's
    name, it saves the contents fo the submitted form's to the proper model.
    ex. contact-us button turns ContactUsForm | newsletter button runs NewsletterForm. """

    multiple_forms(request)

    return render(request, 'aidApp/index.html')


def about_us(request):
    """ newsletter_form checks if the request was post, and if it is saves the contents
    of the submitted form to the newletter model. """

    newsletter_form(request)

    return render(request, 'aidApp/about-us.html')


def login(request):
    return HttpResponse('<h1>Login Page</h1>')


def sign_up(request):
    return HttpResponse('<h1>Sign Up Page</h1>')


def faq(request):

    faqs = FAQ.objects.all()
    context = {
        "faqs": faqs
    }

    newsletter_form(request)

    return render(request, 'aidApp/faq.html', context)
