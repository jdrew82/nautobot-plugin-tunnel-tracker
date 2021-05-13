"""Django views declaration for tunnel_tracker plugin."""

from nautobot.core.views import generic

from .filters import TunnelFilter
from .forms import TunnelCreationForm, TunnelFilterForm, TunnelCreationCSVForm
from .models import Tunnel
from .tables import TunnelTable, TunnelBulkTable


class TunnelListView(generic.ObjectListView):
    """View for listing all Tunnels."""

    queryset = Tunnel.objects.all()
    filterset = TunnelFilter
    filterset_form = TunnelFilterForm
    table = TunnelTable
    action_buttons = ("add", "export")


class TunnelView(generic.ObjectView):
    """View for single Tunnel instance."""

    queryset = Tunnel.objects.all()

    def get_extra_context(self, request, instance):
        """Add extra data to detail view for Nautobot."""
        return {}


class TunnelBulkImportView(generic.BulkImportView):
    """View for bulk-importing a CSV file to create Tunnels."""

    queryset = Tunnel.objects.all()
    model_form = TunnelCreationCSVForm
    table = TunnelBulkTable


class TunnelEditView(generic.ObjectEditView):
    """View for managing Tunnels."""

    queryset = Tunnel.objects.all()
    model_form = TunnelCreationForm


class TunnelDeleteView(generic.ObjectDeleteView):
    """View for deleting Tunnels."""

    queryset = Tunnel.objects.all()


class TunnelBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more Tunnels."""

    queryset = Tunnel.objects.filter()
    table = TunnelTable
