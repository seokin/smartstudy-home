from django.core.urlresolvers import resolve
from models import AppCategory


def extras(request):
    view = ''
    app_categories = AppCategory.objects.all()

    try:
        view = resolve(request.path).url_name
    except:
        pass

    return {
        'view': view,
        'app_categories': app_categories,
    }
