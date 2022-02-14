"""Django views declaration for nautobot_tunnel_tracker plugin."""

import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ToggleColumn
from .models import BaseTunnel, ISAKMPPolicy


class TunnelTable(BaseTable):
    """Table for displaying configured Tunnel instances."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    status = tables.LinkColumn()
    tunnel_type = tables.LinkColumn()
    src_device = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for tunnel_lists.html template to show configured tunnels."""

        model = BaseTunnel
        fields = ["pk", "name", "status", "tunnel_type", "src_device"]


class TunnelBulkTable(BaseTable):
    """Table for displaying Tunnel imports."""

    name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for bulk import of tunnels."""

        model = BaseTunnel
        fields = ("id", "name", "status", "tunnel_type", "src_device")


class ISAKMPPolicyTable(BaseTable):
    """Table for displaying configured ISAKMP Policy instances."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    version = tables.LinkColumn()
    authentication = tables.LinkColumn()
    hash = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for isakmp_policy_lists.html template to show configured ISAKMP policies."""

        model = ISAKMPPolicy
        fields = ["pk", "name", "version", "mode", "authentication", "hash"]


class ISAKMPPolicyBulkTable(BaseTable):
    """Table for displaying ISAKMP Policy imports."""

    name = tables.LinkColumn()
    version = tables.LinkColumn()
    authentication = tables.LinkColumn()
    hash = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for bulk import of ISAKMP Policies."""

        model = ISAKMPPolicy
        fields = ("id", "name", "version", "authentication", "hash")
