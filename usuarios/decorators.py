from django.shortcuts import redirect

def roles_permitidos(roles):
    def decorador(view_func):
        def wrapper(request, *args, **kwargs):
            if request.session.get('rol') not in roles:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorador