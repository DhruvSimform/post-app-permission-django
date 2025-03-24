from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Post  # Import your model

def object_permission_required(permission, model, lookup_field='id', obj_kwarg='post_id'):
    """
    A decorator to check object-level permissions when only the object ID is passed.

    :param permission: The required permission (e.g., 'main.change_post').
    :param model: The model class (e.g., Post).
    :param lookup_field: The field name used to retrieve the object (default: 'id').
    :param obj_kwarg: The keyword argument name that holds the object ID (default: 'post_id').
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            obj_id = kwargs.get(obj_kwarg)
            obj = get_object_or_404(model, **{lookup_field: obj_id})  # Fetch the object

            if not request.user.has_perm(permission, obj):
                raise PermissionDenied  # Return 403 if permission is not granted
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
