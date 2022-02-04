"""Django urlpatterns declaration for nautobot_tunnel_tracker plugin."""

from django.urls import path

from .views import (
    IKEPolicyBulkDeleteView,
    IKEPolicyBulkImportView,
    IKEPolicyEditView,
    IKEPolicyListView,
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
    path("policies/", IKEPolicyListView.as_view(), name="ikepolicy_list"),
    path("policies/add/", IKEPolicyEditView.as_view(), name="ikepolicy_creation"),
    path("policies/delete/", IKEPolicyBulkDeleteView.as_view(), name="ikepolicy_bulk_delete"),
    path("policies/import/", IKEPolicyBulkImportView.as_view(), name="ikepolicy_import"),
]
