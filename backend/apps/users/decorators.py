from django.core.exceptions import PermissionDenied
from functools import wraps


def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied("Usuario no autenticado")

            if getattr(request.user, "role", None) != role:
                raise PermissionDenied("Permiso denegado")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


# Atajos semánticos (opcional pero elegante)
teacher_required = role_required("teacher")
student_required = role_required("student")
admin_required   = role_required("admin")

