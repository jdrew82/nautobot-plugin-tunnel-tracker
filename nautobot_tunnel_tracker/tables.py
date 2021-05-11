"""Django views declaration for nautobot_tunnel_tracker plugin."""

import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ToggleColumn
from .models import Tunnel


class TunnelTable(BaseTable):
    """Table for displaying configured Tunnel instances."""

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for tunnl_lists.html template to show configured tunnels."""

        model = Tunnel
        fields = [
            "pk",
            "name",
            "status",
            "tunnel_type",
            "src_device",
            "dst_device",
            "src_address",
            "dst_address",
        ]


class TunnelBulkTable(BaseTable):
    """Table for displaying Tunnel imports."""

    pk = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for bulk import of tunnels."""

        model = Tunnel
        fields = (
            "pk",
            "name",
            "status",
            "tunnel_type",
            "src_device",
            "dst_device",
            "src_address",
            "dst_address",
        )
