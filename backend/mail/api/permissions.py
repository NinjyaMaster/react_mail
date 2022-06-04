from rest_framework import permissions
from django.db.models import Q

class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.sender


class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)


class IsSenderOrRecipients(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        #if  request.user == obj.recipients:
        print(obj.recipients.all() ) 
        if request.user == obj.sender or (request.user in obj.recipients.all()):
            return True
        return False
        #return bool(request.user == obj.sender or request.user == obj.recipients)
