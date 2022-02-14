"""Django models declaration for nautobot_tunnel_tracker plugin."""

from django.db import models
from django.forms import ValidationError
from django.shortcuts import reverse
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.utils import extras_features

from .choices import (
    ISAKMPAuthenticationChoices,
    DHGroupChoices,
    ISAKMPHashChoices,
    IKEVersionChoices,
    ISAKMPIdentificationMethodChoices,
    ISAKMPModeChoices,
    TunnelStatusChoices,
    TunnelTypeChoices,
    PPTPEncapsulationChoices,
)


class BaseTunnel(PrimaryModel):
    """Base Tunnel model."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=30, choices=TunnelStatusChoices.CHOICES, default=TunnelStatusChoices.STATUS_PENDING_CONFIGURATION
    )
    tunnel_type = models.CharField(
        max_length=30, choices=TunnelTypeChoices.CHOICES, default=TunnelTypeChoices.PPTP_TUNNEL
    )
    src_device = models.ForeignKey(
        to="dcim.Device", on_delete=models.CASCADE, help_text="Source Device", blank=False, related_name="basetunnels"
    )
    src_interface = models.ForeignKey(
        to="dcim.Interface",
        on_delete=models.CASCADE,
        help_text="Source Interface",
        blank=False,
        related_name="basetunnels",
    )

    class Meta:
        """Class to define what will be used to set order based on."""

        abstract = True


@extras_features(
    "custom_fields",
    "custom_validators",
    "export_templates",
    "relationships",
    "graphql",
    "webhooks",
)
class PPTPTunnel(BaseTunnel):
    """PPTP type Tunnel model."""

    dst_device = models.ForeignKey(
        to="dcim.Device",
        on_delete=models.CASCADE,
        help_text="Destination Device",
        blank=False,
        related_name="pptptunnels",
    )
    dst_interface = models.ForeignKey(
        to="dcim.Interface",
        on_delete=models.CASCADE,
        help_text="Destination Interface",
        blank=False,
        related_name="pptptunnels",
    )
    tunnel_mtu = models.IntegerField(help_text="MTU for Tunnel", default=1500)
    clns_mtu = models.IntegerField(help_text="Connectionless-mode Network Service MTU", default=1500)
    encapsulation = models.CharField(
        max_length=30, choices=PPTPEncapsulationChoices.CHOICES, default=PPTPEncapsulationChoices.GRE_ENCAP
    )

    csv_headers = [
        "name",
        "description",
        "status",
        "tunnel_type",
        "src_device",
        "src_interface",
        "dst_device",
        "dst_interface",
        "tunnel_mtu",
        "clns_mtu",
        "encapsulation",
    ]

    def to_csv(self):
        """Indicates model fields to return as csv."""
        return (
            self.name,
            self.description,
            self.status,
            self.tunnel_type,
            self.src_device,
            self.src_interface,
            self.dst_device,
            self.dst_interface,
            self.tunnel_mtu,
            self.clns_mtu,
            self.encapsulation,
        )

    class Meta:
        """Class to define what will be used to set order based on."""

        ordering = ["name"]

    def __str__(self):
        """Class to define what identifies the PPTPTunnel object."""
        return self.name

    def get_absolute_url(self):  # pylint: disable=no-self-use
        """Absolute url for the PPTPTunnel instance."""
        return reverse("plugins:nautobot_tunnel_tracker:tunnels_list")

    def clean(self):
        """Perform validation of model fields."""
        if 0 > self.tunnel_mtu > 9000:
            raise ValidationError(message="Tunnel MTU must be between 0 and 9000.")
        if 0 > self.clns_mtu > 9000:
            raise ValidationError(message="CLNS MTU must be between 0 and 9000.")


class ISAKMPPolicy(PrimaryModel):
    """ISAKMP Policy model."""

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    version = models.CharField(max_length=100, choices=IKEVersionChoices.CHOICES, default=IKEVersionChoices.IKE1)
    mode = models.CharField(max_length=100, choices=ISAKMPModeChoices.CHOICES, default=ISAKMPModeChoices.MAIN)
    identification = models.CharField(
        max_length=100,
        choices=ISAKMPIdentificationMethodChoices.CHOICES,
        default=ISAKMPIdentificationMethodChoices.ADDRESS,
    )
    nat = models.BooleanField(verbose_name="NAT Translation", default=False)
    nat_keepalive = models.IntegerField(verbose_name="NAT Keepalive", default=3600)
    authentication = models.CharField(
        max_length=100, choices=ISAKMPAuthenticationChoices.CHOICES, default=ISAKMPAuthenticationChoices.PRE_SHARED_KEY
    )
    hash = models.CharField(max_length=100, choices=ISAKMPHashChoices.CHOICES, default=ISAKMPHashChoices.HMAC_MD5)
    dh_group = models.CharField(max_length=100, choices=DHGroupChoices.CHOICES, default=DHGroupChoices.GROUP1)
    pfs = models.BooleanField(verbose_name="Perfect Forward Secrecy", default=False)
    lifetime = models.IntegerField(verbose_name="SA Lifetime", default=86400)
    secrets_group = models.ForeignKey(
        to="extras.SecretsGroup",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Secrets Group to use for authentication. Should contain a Generic Secret or Key pointing to the relevant Secret.",
    )

    csv_headers = [
        "name",
        "description",
        "version",
        "identification",
        "nat",
        "nat_keepalive",
        "authentication",
        "hash",
        "dh_group",
        "pfs",
        "lifetime",
    ]

    def to_csv(self):
        """Indicates model fields to return as csv."""
        return (
            self.name,
            self.description,
            self.version,
            self.identification,
            self.nat,
            self.nat_keepalive,
            self.authentication,
            self.hash,
            self.dh_group,
            self.pfs,
            self.lifetime,
        )

    def __str__(self):
        """Class to define what identifies the ISAKMP Policy object."""
        return self.name

    def get_absolute_url(self):  # pylint: disable=no-self-use
        """Absolute url for the ISAKMP Policy instance."""
        return reverse("plugins:nautobot_tunnel_tracker:isakmppolicy_list")

    def clean(self):
        """Perform validation of model fields."""
        if 0 > self.lifetime > 2147483647:
            raise ValidationError("Lifetime must be greater than 0 and less than 2147483647.")
        if 10 > self.nat_keepalive > 3600:
            raise ValidationError(message="NAT Keepalive must be between 10 and 3600.")
