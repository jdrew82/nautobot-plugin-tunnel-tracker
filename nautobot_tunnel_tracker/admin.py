"""Django models declaration for nautobot_tunnel_tracker plugin."""

from django.contrib import admin
from .models import Tunnel


@admin.register(Tunnel)
class TunnelAdmin(admin.ModelAdmin):
    """Administrative view for managing Tunnels instances."""

    list_display = ("tunnel_id", "name", "status", "tunnel_type")
