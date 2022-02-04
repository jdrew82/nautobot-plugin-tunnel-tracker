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
    PPTP_TUNNEL = "pptp-tunnel"
    L2TP_TUNNEL = "l2tp-tunnel"
    CIPE_TUNNEL = "cipe-tunnel"

    CHOICES = (
        (IPSEC_TUNNEL, "IPSec Tunnel"),
        (PPTP_TUNNEL, "PPTP Tunnel"),
        (L2TP_TUNNEL, "L2TP Tunnel"),
        (CIPE_TUNNEL, "CIPE Tunnel"),
    )


class PPTPEncapsulationChoices(ChoiceSet):
    """List of possible types of encapsulation for a PPTP Tunnel."""

    GRE_ENCAP = "gre"
    PAP_ENCAP = "pap"
    CHAP_ENCAP = "chap"
    MSCHAP_ENCAP = "mschap"
    MSCHAP2_ENCAP = "mschap2"
    MPPE_ENCAP = "mppe"

    CHOICES = (
        (GRE_ENCAP, "GRE Encapsulation"),
        (PAP_ENCAP, "PAP Encapsulation"),
        (CHAP_ENCAP, "CHAP Encapsulation"),
        (MSCHAP_ENCAP, "Microsoft CHAPv1 Encapsulation"),
        (MSCHAP2_ENCAP, "Microsoft CHAPv2 Encapsulation"),
        (MPPE_ENCAP, "MPPE Encapsulation"),
    )

