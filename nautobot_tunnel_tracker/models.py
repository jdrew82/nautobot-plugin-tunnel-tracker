"""Django models declaration for nautobot_tunnel_tracker plugin."""

from django.db import models
from django.shortcuts import reverse
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.utils import extras_features

from .choices import TunnelStatusChoices, TunnelTypeChoices


@extras_features(
    "custom_fields",
    "custom_validators",
    "export_templates",
    "relationships",
    "graphql",
    "webhooks",
)
class BaseTunnel(PrimaryModel):
    """Base Tunnel model."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=30, choices=TunnelStatusChoices, default=TunnelStatusChoices.STATUS_PENDING_CONFIGURATION
    )
    tunnel_type = models.CharField(max_length=30, choices=TunnelTypeChoices, default=TunnelTypeChoices.PPTP_TUNNEL)
    src_device = models.OneToOneField(
        to="dcim.Device", on_delete=models.CASCADE, help_text="Source Device", blank=False
    )
    src_interface = models.OneToOneField(
        to="dcim.Interface",
        on_delete=models.CASCADE,
        help_text="Source Interface",
        blank=False,
        limit_choices_to=models.Q(app_label="dcim", model="interface", device_name=src_device),
    )

    csv_headers = [
        "name",
        "description",
        "status",
        "tunnel_type",
        "src_device",
        "src_interface",
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
        )

    class Meta:
        """Class to define what will be used to set order based on."""

        ordering = ["name"]

    def __str__(self):
        """Class to define what identifies the BaseTunnel object."""
        return self.name

    def get_absolute_url(self):  # pylint: disable=no-self-use
        """Absolute url for the Tunnel instance."""
        return reverse("plugins:nautobot_tunnel_tracker:tunnels_list")

    def clean(self):
        """Clean method for BaseTunnel class."""
        super().clean()

    def save(self, *args, **kwargs):
        """Save method for BaseTunnel class."""
        return super().save(*args, **kwargs)


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

    dst_device = models.OneToOneField(
        to="dcim.Device", on_delete=models.CASCADE, help_text="Destination Device", blank=False
    )
    dst_interface = models.OneToOneField(
        to="dcim.Interface",
        on_delete=models.CASCADE,
        help_text="Destination Interface",
        blank=False,
        limit_choices_to=models.Q(app_label="dcim", model="interface", device_name=dst_device),
    )
    tunnel_mtu = models.IntegerField(help_text="MTU for Tunnel", default=1500)
    clns_mtu = models.IntegerField(help_text="Connectionless-mode Network Service MTU", default=1500)
    encapsulation = models.CharField(
        max_length=30, choices=PPTPEncapsulationChoices, default=PPTPEncapsulationChoices.GRE_ENCAP
    )

    csv_headers = ["name", "description", "status", "tunnel_type", "src_device", ""]

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
        """Clean method for PPTPTunnel class."""
        super().clean()

    def save(self, *args, **kwargs):
        """Save method for PPTPTunnel class."""
        return super().save(*args, **kwargs)

