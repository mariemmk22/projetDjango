from django.shortcuts import redirect
from django.http import HttpResponse


def notLoggedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('../')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('accueil')

        return wrapper_func
    return decorator


def forAdmins(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        elif group == 'custumer':
            return redirect('accueil')
        else:
            # Handle other cases, e.g., redirect to an error page
            return HttpResponse("Unauthorized", status=401)

    return wrapper_func
