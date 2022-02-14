"""Django views declaration for tunnel_tracker plugin."""

from nautobot.core.views import generic

from .filters import TunnelFilter, ISAKMPPolicyFilter
from .forms import (
    TunnelCreationForm,
    TunnelFilterForm,
    TunnelCreationCSVForm,
    ISAKMPPolicyCreationForm,
    ISAKMPPolicyFilterForm,
    ISAKMPPolicyCreationCSVForm,
)
from .models import ISAKMPPolicy, PPTPTunnel
from .tables import TunnelTable, TunnelBulkTable, ISAKMPPolicyTable, ISAKMPPolicyBulkTable


class TunnelListView(generic.ObjectListView):
    """View for listing all Tunnels."""

    queryset = PPTPTunnel.objects.all()
    filterset = TunnelFilter
    filterset_form = TunnelFilterForm
    table = TunnelTable
    template_name = "nautobot_tunnel_tracker/tunnel_list.html"


class TunnelView(generic.ObjectView):
    """View for single Tunnel instance."""

    queryset = PPTPTunnel.objects.all()

    def get_extra_context(self, request, instance):
        """Add extra data to detail view for Nautobot."""
        return {}


class TunnelBulkImportView(generic.BulkImportView):
    """View for bulk-importing a CSV file to create Tunnels."""

    queryset = PPTPTunnel.objects.all()
    model_form = TunnelCreationCSVForm
    table = TunnelBulkTable


class TunnelEditView(generic.ObjectEditView):
    """View for managing Tunnels."""

    queryset = PPTPTunnel.objects.all()
    model_form = TunnelCreationForm


class TunnelDeleteView(generic.ObjectDeleteView):
    """View for deleting Tunnels."""

    queryset = PPTPTunnel.objects.all()


class TunnelBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more Tunnels."""

    queryset = PPTPTunnel.objects.filter()
    table = TunnelTable


class ISAKMPPolicyListView(generic.ObjectListView):
    """View for listing all ISAKMP Policies."""

    queryset = ISAKMPPolicy.objects.all()
    filterset = ISAKMPPolicyFilter
    filterset_form = ISAKMPPolicyFilterForm
    table = ISAKMPPolicyTable
    template_name = "nautobot_tunnel_tracker/isakmp_policy_list.html"


class ISAKMPPolicyView(generic.ObjectView):
    """View for single ISAKMP Policy instance."""

    queryset = ISAKMPPolicy.objects.all()

    def get_extra_context(self, request, instance):
        """Add extra data to detail view for Nautobot."""
        return {}


class ISAKMPPolicyBulkImportView(generic.BulkImportView):
    """View for bulk-importing a CSV file to create ISAKMP Policies."""

    queryset = ISAKMPPolicy.objects.all()
    model_form = ISAKMPPolicyCreationCSVForm
    table = ISAKMPPolicyBulkTable


class ISAKMPPolicyEditView(generic.ObjectEditView):
    """View for managing ISAKMP Policies."""

    queryset = ISAKMPPolicy.objects.all()
    model_form = ISAKMPPolicyCreationForm


class ISAKMPPolicyDeleteView(generic.ObjectDeleteView):
    """View for deleting ISAKMP Policies."""

    queryset = ISAKMPPolicy.objects.all()


class ISAKMPPolicyBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more ISAKMP Policies."""

    queryset = ISAKMPPolicy.objects.filter()
    table = ISAKMPPolicyTable
