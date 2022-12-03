from rest_framework.permissions import BasePermission

class InchargePermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'In'


class StudentPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'St'