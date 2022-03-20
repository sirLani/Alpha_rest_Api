from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit  their own profil"""

    def has_object_permission(self, request, obj):
        """Check user is trying to edit theri own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permissison(self, request, view, obj):
        """check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
