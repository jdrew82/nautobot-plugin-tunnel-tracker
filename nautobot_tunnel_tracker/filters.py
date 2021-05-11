"""Django filters declaration for nautobot_tunnel_tracker plugin."""

import django_filters
from django.db.models import Q

from nautobot.extras.filters import CreatedUpdatedFilterSet

from .models import Tunnel


class TunnelFilter(CreatedUpdatedFilterSet):
    """Filter capabilities for Tunnel instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    name = django_filters.ModelMultipleChoiceFilter(
        field_name="name__slug",
        queryset=Tunnel.objects.all(),
        to_field_name="slug",
        label="Tunnel Name (slug)",
    )

    status = django_filters.ModelMultipleChoiceFilter(
        field_name="status__slug",
        queryset=Tunnel.objects.all(),
        to_field_name="slug",
        label="Tunnel Status (slug)",
    )

    tunnel_type = django_filters.ModelMultipleChoiceFilter(
        field_name="tunnel_type__slug",
        queryset=Tunnel.objects.all(),
        to_field_name="slug",
        label="Tunnel Type (slug)",
    )

    class Meta:
        """Class to define what is used for filtering tunnels with the search box."""

        model = Tunnel
        fields = ["name", "status", "tunnel_type"]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(status__icontains=value) | Q(tunnel_type__icontains=value)
        return queryset.filter(qs_filter)
