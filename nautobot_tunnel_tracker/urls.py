"""Django urlpatterns declaration for nautobot_tunnel_tracker plugin."""

from django.urls import path

from .views import (
    ListTunnelView,
    CreateTunnelView,
    BulkDeleteTunnelView,
    BulkImportTunnelView,
)

urlpatterns = [
    path("", ListTunnelView.as_view(), name="tunnels_list"),
    path("add/", CreateTunnelView.as_view(), name="tunnel_creation"),
    path("delete/", BulkDeleteTunnelView.as_view(), name="tunnels_bulk_delete"),
    path("import/", BulkImportTunnelView.as_view(), name="tunnels_import"),
]
