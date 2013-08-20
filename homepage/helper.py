from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def sendResumeLink(request, resume):
    variables = Context({
        'request': request,
        'resume': resume,
    })
    html = get_template('mail/resume_link.html').render(variables)
    text = get_template('mail/resume_link_text.html').render(variables)

    msg = EmailMultiAlternatives(
        settings.EMAIL_RESUME_TITLE,
        text,
        settings.EMAIL_SENDER,
        [resume.email])
    msg.attach_alternative(html, "text/html")

    try:
        msg.send(fail_silently=False)
    except:
        pass
