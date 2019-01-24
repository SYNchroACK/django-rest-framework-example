from rest_framework import filters

from django.db.models import Q


class IsOwnerOrPublicFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        q_public = Q(public=True)
        q_owner = Q(user=request.user.id)

        return queryset.filter(q_owner|q_public)