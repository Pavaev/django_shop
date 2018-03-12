from django.http import HttpResponseBadRequest


def required_AJAX(function):
    def wrap(request, *args, **kwargs):
        if request.is_ajax():
            return function(request, *args, **kwargs)
        else:
            return HttpResponseBadRequest()

    wrap.__name__ = function.__name__
    wrap.__doc__ = function.__doc__
    return wrap
