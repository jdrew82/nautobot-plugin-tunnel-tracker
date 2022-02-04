"""Django filters declaration for nautobot_tunnel_tracker plugin."""

import django_filters
from django.db.models import Q

from nautobot.extras.filters import CreatedUpdatedFilterSet

from .models import BaseTunnel, IKEPolicy


class TunnelFilter(CreatedUpdatedFilterSet):
    """Filter capabilities for Tunnel instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    name = django_filters.ModelMultipleChoiceFilter(
        field_name="name",
        queryset=BaseTunnel.objects.all(),
        to_field_name="slug",
        label="Tunnel Name",
    )

    status = django_filters.ModelMultipleChoiceFilter(
        field_name="status",
        queryset=BaseTunnel.objects.all(),
        to_field_name="slug",
        label="Tunnel Status",
    )

    tunnel_type = django_filters.ModelMultipleChoiceFilter(
        field_name="tunnel_type",
        queryset=BaseTunnel.objects.all(),
        to_field_name="slug",
        label="Tunnel Type",
    )

    class Meta:
        """Class to define what is used for filtering tunnels with the search box."""

        model = BaseTunnel
        fields = ["name", "status", "tunnel_type"]

    def search(self, queryset, value):  # pylint: disable=no-self-use
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(status__icontains=value) | Q(tunnel_type__icontains=value)
        return queryset.filter(qs_filter)
