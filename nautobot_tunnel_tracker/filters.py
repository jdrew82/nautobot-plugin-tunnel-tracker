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


class IKEPolicyFilter(CreatedUpdatedFilterSet):
    """Filter capabilities for IKE Policy instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    name = django_filters.ModelMultipleChoiceFilter(
        field_name="name",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy Name",
    )

    version = django_filters.ModelMultipleChoiceFilter(
        field_name="version",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy Version",
    )

    nat = django_filters.ModelMultipleChoiceFilter(
        field_name="nat",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy NAT Translation",
    )

    authentication = django_filters.ModelMultipleChoiceFilter(
        field_name="authentication",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy Authentication",
    )

    hash = django_filters.ModelMultipleChoiceFilter(
        field_name="hash",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy Hash",
    )

    dh_group = django_filters.ModelMultipleChoiceFilter(
        field_name="dh_group",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy DH Group",
    )

    pfs = django_filters.ModelMultipleChoiceFilter(
        field_name="pfs",
        queryset=IKEPolicy.objects.all(),
        to_field_name="slug",
        label="IKE Policy PFS",
    )

    class Meta:
        """Class to define what is used for filtering IKE policies with the search box."""

        model = IKEPolicy
        fields = ["name", "version", "nat", "authentication", "hash", "dh_group", "pfs"]

    def search(self, queryset, value):  # pylint: disable=no-self-use
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(version__icontains=value)
            | Q(nat__icontains=value)
            | Q(authentication__icontains=value)
            | Q(hash__icontains=value)
            | Q(dh_group__icontains=value)
            | Q(pfs__icontains=value)
        )
        return queryset.filter(qs_filter)
