from django.core.mail import send_mail
from django.contrib import messages

from.forms import ContactUsForm, NewsletterForm

""" multiple_forms checks if the request was post. If it is then,
it checks for the name of the submitted form's submit button to match premade options
if it does it will go to the appropriate form's function. """


def multiple_forms(request):
    if request.method == "POST":
        if 'contact-us' in request.POST:
            contact_us_form_handling(request)
        elif 'newsletter' in request.POST:
            newsletter_form_handling(request)
            """ for more forms simply add more elifs, and call the handling function for it.
            the function does not need to check if the requst is post, as it is already done here. """
        else:
            messages.warning(request, 'Something went Wrong')


""" newsletter_form checks if the request was post. If it is then,
it will go to the newsletter form function. """


def newsletter_form(request):
    if request.method == 'POST':
        newsletter_form_handling(request)


""" newsletter_form_handling loads the newsletter form from an already checked post request,
if it is a valid form, it will then send an email to the subcriber and write a message on the page
if it is not a valid form(email already exists) it will inform the subscriber that they are
already subscribed.
there is already html validation so only thing that can be wrong is already existing email. """


def newsletter_form_handling(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        email = [form.cleaned_data['email']]

        send_mail(
            subject='Thank You for subscribing to our Newsletter',
            message='You are now subscribed to our newletter. you can expect all the best news straight form the source!',
            from_email=None,
            recipient_list=email,
            fail_silently=False
        )

        form.save()
        messages.success(
            request, 'Thank you for subscribing to our newsletter!')
    else:
        messages.info(
            request, 'You are already subscribed to our newsletter!')


""" contact_us_form_handling loads the contact us form from an already checked post request,
if it is a valid form, it will then send an email to the user and write a message on the page
if it is not a valid form it will inform the user that something went wrong,
there is already html validatoin so I am not sure what could possibly go wrong. """


def contact_us_form_handling(request):
    form = ContactUsForm(request.POST)
    if form.is_valid():
        email = [form.cleaned_data['email']]

        send_mail(
            subject='Thank You for Your Inquiry',
            message='Your inquiry has been received. We will respond as soon as we can.',
            from_email=None,
            recipient_list=email,
            fail_silently=False
        )

        form.save()
        messages.success(
            request, 'Thank you for your inquiry!'
        )
    else:
        messages.warning(
            request,
            'There was an unexpected error. Please try again later.'
        )
