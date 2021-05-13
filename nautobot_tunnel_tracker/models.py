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
class Tunnel(PrimaryModel):
    """Tunnel model."""

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=30, choices=TunnelStatusChoices, default=TunnelStatusChoices.STATUS_PENDING_CONFIGURATION
    )
    tunnel_type = models.CharField(max_length=30, choices=TunnelTypeChoices, default=TunnelTypeChoices.PPTP_TUNNEL)
    src_device = models.OneToOneField(
        to="dcim.Device", on_delete=models.CASCADE, help_text="Source Device", blank=False
    )
    tunnel_mtu = models.IntegerField(help_text="MTU for tunnel", default=1500)
    clns_mtu = models.IntegerField(help_text="Connectionless-mode Network Service MTU", default=1500)

    csv_headers = [
        "name",
        "status",
        "tunnel_type",
        "src_device",
        "tunnel_mtu",
        "clns_mtu",
    ]

    def to_csv(self):
        """Indicates model fields to return as csv."""
        return (
            self.name,
            self.status,
            self.tunnel_type,
            self.src_device,
            self.src_address,
            self.dst_address,
        )

    class Meta:
        """Class to define what will be used to set order based on. Will be using the unique tunnel ID for this purpose."""

        ordering = ["name"]

    def __str__(self):
        """Class to define what identifies the Tunnel object. Will be using name for this."""
        return self.name

    def get_absolute_url(self):
        """Absolute url for the Tunnel instance."""
        return reverse("plugins:nautobot_tunnel_tracker:tunnels_list")
