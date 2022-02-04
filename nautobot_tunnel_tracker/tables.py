"""Django views declaration for nautobot_tunnel_tracker plugin."""

import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ToggleColumn
from .models import BaseTunnel, IKEPolicy


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


class IKEPolicyTable(BaseTable):
    """Table for displaying configured IKE Policy instances."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    version = tables.LinkColumn()
    authentication = tables.LinkColumn()
    hash = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for ikepolicy_lists.html template to show configured IKE policies."""

        model = IKEPolicy
        fields = ["pk", "name", "version", "authentication", "hash"]


class IKEPolicyBulkTable(BaseTable):
    """Table for displaying IKE Policy imports."""

    name = tables.LinkColumn()
    version = tables.LinkColumn()
    authentication = tables.LinkColumn()
    hash = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for bulk import of IKE Policies."""

        model = IKEPolicy
        fields = ("id", "name", "version", "authentication", "hash")
