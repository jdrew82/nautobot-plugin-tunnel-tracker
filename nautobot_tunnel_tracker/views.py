"""Django views declaration for tunnel_tracker plugin."""

from nautobot.core.views import generic

from .filters import TunnelFilter, IKEPolicyFilter
from .forms import (
    TunnelCreationForm,
    TunnelFilterForm,
    TunnelCreationCSVForm,
    IKEPolicyCreationForm,
    IKEPolicyFilterForm,
    IKEPolicyCreationCSVForm,
)
from .models import BaseTunnel, IKEPolicy
from .tables import TunnelTable, TunnelBulkTable, IKEPolicyTable, IKEPolicyBulkTable


class TunnelListView(generic.ObjectListView):
    """View for listing all Tunnels."""

    queryset = BaseTunnel.objects.all()
    filterset = TunnelFilter
    filterset_form = TunnelFilterForm
    table = TunnelTable
    template_name = "nautobot_tunnel_tracker/tunnel_list.html"


class TunnelView(generic.ObjectView):
    """View for single Tunnel instance."""

    queryset = BaseTunnel.objects.all()

    def get_extra_context(self, request, instance):
        """Add extra data to detail view for Nautobot."""
        return {}


class TunnelBulkImportView(generic.BulkImportView):
    """View for bulk-importing a CSV file to create Tunnels."""

    queryset = BaseTunnel.objects.all()
    model_form = TunnelCreationCSVForm
    table = TunnelBulkTable


class TunnelEditView(generic.ObjectEditView):
    """View for managing Tunnels."""

    queryset = BaseTunnel.objects.all()
    model_form = TunnelCreationForm


class TunnelDeleteView(generic.ObjectDeleteView):
    """View for deleting Tunnels."""

    queryset = BaseTunnel.objects.all()


class TunnelBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more Tunnels."""

    queryset = BaseTunnel.objects.filter()
    table = TunnelTable


class IKEPolicyListView(generic.ObjectListView):
    """View for listing all IKE Policies."""

    queryset = IKEPolicy.objects.all()
    filterset = IKEPolicyFilter
    filterset_form = IKEPolicyFilterForm
    table = IKEPolicyTable
    template_name = "nautobot_tunnel_tracker/ikepolicy_list.html"


class IKEPolicyView(generic.ObjectView):
    """View for single IKE Policy instance."""

    queryset = IKEPolicy.objects.all()

    def get_extra_context(self, request, instance):
        """Add extra data to detail view for Nautobot."""
        return {}


class IKEPolicyBulkImportView(generic.BulkImportView):
    """View for bulk-importing a CSV file to create IKE Policies."""

    queryset = IKEPolicy.objects.all()
    model_form = IKEPolicyCreationCSVForm
    table = IKEPolicyBulkTable


class IKEPolicyEditView(generic.ObjectEditView):
    """View for managing IKE Policies."""

    queryset = IKEPolicy.objects.all()
    model_form = IKEPolicyCreationForm


class IKEPolicyDeleteView(generic.ObjectDeleteView):
    """View for deleting IKE Policies."""

    queryset = IKEPolicy.objects.all()


class IKEPolicyBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more IKE Policies."""

    queryset = IKEPolicy.objects.filter()
    table = IKEPolicyTable
