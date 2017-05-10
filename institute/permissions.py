from rest_framework import permissions

class IsAuthorOfInstitute(permissions.BasePermission):
    def has_object_permission(self, request, view, institute):
        if request.user:
            return institute.author == request.user
        return False