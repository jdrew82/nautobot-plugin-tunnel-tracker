"""Django navigation declaration for nautobot_tunnel_tracker plugin."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:nautobot_tunnel_tracker:tunnels_list",
        link_text="PPTP Tunnels",
        permissions=["nautobot_tunnel_tracker.view_tunnels"],
        buttons=(
            # Link to the plugins view to add a tunnel if user has "add_tunnels" permission.
            PluginMenuButton(
                link="plugins:nautobot_tunnel_tracker:tunnel_creation",
                title="Add a new PPTP tunnel",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_tunnel_tracker.add_tunnels"],
            ),
            # Links to the plugins view to bulk import tunnels if user has the "add_tunnels" permission.
            PluginMenuButton(
                link="plugins:nautobot_tunnel_tracker:tunnels_import",
                title="Bulk import PPTP tunnels",
                icon_class="mdi mdi-database-import-outline",
                color=ButtonColorChoices.BLUE,
                permissions=["nautobot_tunnel_tracker.add_tunnels"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:nautobot_tunnel_tracker:ikepolicy_list",
        link_text="IKE Policies",
        permissions=["nautobot_tunnel_tracker.view_ikepolicy"],
        buttons=(
            # Link to the plugins view to add a tunnel if user has "add_tunnels" permission.
            PluginMenuButton(
                link="plugins:nautobot_tunnel_tracker:ikepolicy_creation",
                title="Add a new IKE Policy",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_tunnel_tracker.add_ikepolicy"],
            ),
            # Links to the plugins view to bulk import tunnels if user has the "add_tunnels" permission.
            PluginMenuButton(
                link="plugins:nautobot_tunnel_tracker:ikepolicy_import",
                title="Bulk import IKE Policy",
                icon_class="mdi mdi-database-import-outline",
                color=ButtonColorChoices.BLUE,
                permissions=["nautobot_tunnel_tracker.add_ikepolicy"],
            ),
        ),
    ),
)
