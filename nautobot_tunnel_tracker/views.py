"""Django views declaration for tunnel_tracker plugin."""

from django.contrib.auth.mixins import PermissionRequiredMixin
from nautobot.core.views import generic

from .filters import TunnelFilter
from .forms import TunnelCreationForm, TunnelFilterForm, TunnelCreationCSVForm
from .models import Tunnel
from .tables import TunnelTable, TunnelBulkTable


class ListTunnelView(PermissionRequiredMixin, generic.ObjectListView):
    """View for listing all Tunnels."""

    permission_required = "nautobot_tunnel_tracker.view_tunnels"
    model = Tunnel
    queryset = Tunnel.objects.all().order_by("tunnel_id")
    filterset = TunnelFilter
    filterset_form = TunnelFilterForm
    table = TunnelTable
    template_name = "tunnels_list.html"


class CreateTunnelView(PermissionRequiredMixin, generic.ObjectEditView):
    """View for creating a new Tunnels."""

    permission_required = "nautobot_tunnel_tracker.add_tunnels"
    model = Tunnel
    queryset = Tunnel.objects.all()
    model_form = TunnelCreationForm
    template_name = "tunnel_edit.html"
    default_return_url = "plugins:nautobot_tunnel_tracker:tunnels_list"


class BulkDeleteTunnelView(PermissionRequiredMixin, generic.BulkDeleteView):
    """View for deleting one or more Tunnels."""

    permission_required = "nautobot_tunnel_tracker.delete_tunnels"
    queryset = Tunnel.objects.filter()
    table = TunnelTable
    default_return_url = "plugins:nautobot_tunnel_tracker:tunnels_list"


class BulkImportTunnelView(PermissionRequiredMixin, generic.BulkImportView):
    """View for bulk-importing a CSV file to create Tunnels."""

    permission_required = "nautobot_tunnel_tracker.add_tunnels"
    model_form = TunnelCreationCSVForm
    tunnel = TunnelBulkTable
    default_return_url = "plugins:nautobot_tunnel_tracker:tunnels_list"
