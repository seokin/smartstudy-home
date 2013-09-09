from django.template.loader import get_template
from django.template import Context, Template
from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings
from email.mime.image import MIMEImage


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


def sendResumeInformMail(request, resumes):
    top_image = None
    bottom_image = None

    if request.FILES.get('top_image'):
        top_image = MIMEImage(request.FILES['top_image'].read())
        top_image.add_header('Content-ID', '<top_image>')

    if request.FILES.get('bottom_image'):
        bottom_image = MIMEImage(request.FILES['bottom_image'].read())
        bottom_image.add_header('Content-ID', '<bottom_image>')

    username = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD

    if request.POST.get('mail_password'):
        username = request.user.email
        password = request.POST.get('mail_password')

        print username, password

    connection = get_connection(host=settings.EMAIL_HOST,
                                port=settings.EMAIL_PORT,
                                username=username,
                                password=password,
                                user_tls=settings.EMAIL_USE_TLS)

    for resume in resumes:
        subject = request.POST.get('subject')
        password = request.POST.get('password')
        message_template = Template(request.POST.get('message'))
        message = message_template.render(Context({
            'resume': resume,
        }))

        variables = Context({
            'resume': resume,
            'message': message,
            'top_image': top_image,
            'bottom_image': bottom_image,
        })

        html = get_template('mail/resume_inform.html').render(variables)
        text = get_template('mail/resume_inform_text.html').render(variables)

        msg = EmailMultiAlternatives(
            subject,
            text,
            '%s%s <%s>' % (request.user.last_name, request.user.first_name, request.user.email),
            [resume.email])
        msg.attach_alternative(html, "text/html")
        msg.content_subtype = 'html'
        msg.connection = connection

        if top_image:
            msg.attach(top_image)

        if bottom_image:
            msg.attach(bottom_image)

        try:
            msg.send(fail_silently=False)
        except:
            pass
