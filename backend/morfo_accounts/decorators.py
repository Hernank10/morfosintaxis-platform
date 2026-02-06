from django.core.exceptions import PermissionDenied
from functools import wraps

def teacher_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Usuario no autenticado")

        if request.user.role != "teacher" and request.user.role != "admin":
            raise PermissionDenied("Solo profesores pueden realizar esta acción")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
