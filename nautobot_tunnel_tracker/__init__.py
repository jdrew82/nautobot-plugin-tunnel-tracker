"""Plugin declaration for nautobot_tunnel_tracker."""

__version__ = "0.2.0"

from nautobot.extras.plugins import PluginConfig


class TunnelTrackerConfig(PluginConfig):
    """Plugin configuration for the nautobot_tunnel_tracker plugin."""

    name = "nautobot_tunnel_tracker"
    verbose_name = "Nautobot Tunnel Tracker"
    version = __version__
    author = "Justin Drew"
    description = "Nautobot Tunnel Tracker."
    base_url = "tunnel-tracker"
    required_settings = []
    min_version = "1.0.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = TunnelTrackerConfig  # pylint:disable=invalid-name
