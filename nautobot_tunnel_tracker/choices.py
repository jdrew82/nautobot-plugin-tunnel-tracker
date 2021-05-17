"""Django forms declaration for nautobot_tunnel_tracker plugin."""

from nautobot.utilities.choices import ChoiceSet


class TunnelStatusChoices(ChoiceSet):
    """List of possible status for a Tunnel."""

    STATUS_PENDING_CONFIGURATION = "pending-configuration"
    STATUS_CONFIGURED = "configured"
    STATUS_PENDING_DELETION = "pending-deletion"

    CHOICES = (
        (STATUS_PENDING_CONFIGURATION, "Pending Configuration"),
        (STATUS_CONFIGURED, "Configured"),
        (STATUS_PENDING_DELETION, "Pending Deletion"),
    )


class TunnelTypeChoices(ChoiceSet):
    """List of possible types of Tunnels."""

    IPSEC_TUNNEL = "ipsec-tunnel"
    GRE_TUNNEL = "gre-tunnel"
    L2TP_TUNNEL = "l2tp-tunnel"
    CIPE_TUNNEL = "cipe-tunnel"

    CHOICES = (
        (IPSEC_TUNNEL, "IPSec Tunnel"),
        (GRE_TUNNEL, "GRE Tunnel"),
        (L2TP_TUNNEL, "L2TP Tunnel"),
        (CIPE_TUNNEL, "CIPE Tunnel"),
    )
