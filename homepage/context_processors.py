from django.core.urlresolvers import resolve


def extras(request):
    view = ''

    try:
        view = resolve(request.path).url_name
    except:
        pass

    return {
        'view': view,
    }
