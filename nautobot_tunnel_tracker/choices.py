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


class IKEVersionChoices(ChoiceSet):
    """List of possible types of IKE."""

    IKE1 = "ike1"
    IKE2 = "ike2"

    CHOICES = (
        (IKE1, "IKEv1"),
        (IKE2, "IKEv2"),
    )


class ISAKMPModeChoices(ChoiceSet):
    """List of possible ISAKMP modes."""

    AGGRESSIVE = "aggressive"
    MAIN = "main"

    CHOICES = (
        (AGGRESSIVE, "Aggressive"),
        (MAIN, "Main"),
    )


class ISAKMPIdentificationMethodChoices(ChoiceSet):
    """List of possible ISAKMP identification methods."""

    ADDRESS = "address"
    AUTOMATIC = "automatic"
    HOSTNAME = "hostname"
    KEY_ID = "key"

    CHOICES = (
        (ADDRESS, "Address"),
        (AUTOMATIC, "Automatic"),
        (HOSTNAME, "Hostname"),
        (KEY_ID, "Key ID"),
    )


class ISAKMPAuthenticationChoices(ChoiceSet):
    """List of possible ISAKMP authentication types."""

    PRE_SHARED_KEY = "pre-share"
    CERTIFICATE = "rsa-sig"
    CRACK = "crack"

    CHOICES = (
        (PRE_SHARED_KEY, "Pre-shared Key"),
        (CERTIFICATE, "Certificate"),
        (CRACK, "Challenge/Response for Auth Crypto Keys"),
    )


class ISAKMPHashChoices(ChoiceSet):
    """List of possible ISAKMP hashing types."""

    HMAC_MD5 = "hmac-md5"
    HMAC_SHA = "hmac-sha1"

    CHOICES = (
        (HMAC_MD5, "HMAC-MD5"),
        (HMAC_SHA, "HMAC-SHA1"),
    )


class ISAKMPEncryptionChoices(ChoiceSet):
    """List of possible ISAKMP encryption types."""

    DES = "des"
    TRIPLEDES = "3des"
    AES = "aes"
    AES_192 = "aes-192"
    AES_256 = "aes-256"

    CHOICES = (
        (DES, "DES"),
        (TRIPLEDES, "3DES"),
        (AES, "AES (128 bits)"),
        (AES_192, "AES (192 bits)"),
        (AES_256, "AES (256 bits)"),
    )


class DHGroupChoices(ChoiceSet):
    """List of possible Diffie-Hellman groups."""

    GROUP1 = "group1"
    GROUP2 = "group2"
    GROUP5 = "group5"
    GROUP7 = "group7"
    GROUP14 = "group14"
    GROUP19 = "group19"
    GROUP20 = "group20"

    CHOICES = (
        (GROUP1, "Group 1 (768 bits)"),
        (GROUP2, "Group 2 (1024 bits)"),
        (GROUP5, "Group 5 (1536 bits)"),
        (GROUP7, "Group 7 (163 bits EC)"),
        (GROUP14, "Group 14 (2048 bits)"),
        (GROUP19, "Group 19 (256 bits EC)"),
        (GROUP20, "Group 20 (384 bits EC)"),
    )
