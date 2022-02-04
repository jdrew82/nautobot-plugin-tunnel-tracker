"""Django urlpatterns declaration for nautobot_tunnel_tracker plugin."""

from django.urls import path

from .views import (
    TunnelListView,
    TunnelEditView,
    TunnelBulkDeleteView,
    TunnelBulkImportView,
)

urlpatterns = [
    path("tunnels/", TunnelListView.as_view(), name="tunnels_list"),
    path("tunnels/add/", TunnelEditView.as_view(), name="tunnel_creation"),
    path("tunnels/delete/", TunnelBulkDeleteView.as_view(), name="tunnels_bulk_delete"),
    path("tunnels/import/", TunnelBulkImportView.as_view(), name="tunnels_import"),
    path("", TunnelListView.as_view(), name="tunnels_list"),
    path("add/", TunnelEditView.as_view(), name="tunnel_creation"),
    path("delete/", TunnelBulkDeleteView.as_view(), name="tunnels_bulk_delete"),
    path("import/", TunnelBulkImportView.as_view(), name="tunnels_import"),
]
