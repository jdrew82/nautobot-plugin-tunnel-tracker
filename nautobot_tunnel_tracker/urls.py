"""Django urlpatterns declaration for nautobot_tunnel_tracker plugin."""

from django.urls import path

from .views import (
    ISAKMPPolicyBulkDeleteView,
    ISAKMPPolicyBulkImportView,
    ISAKMPPolicyEditView,
    ISAKMPPolicyListView,
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
    path("isakmp_policies/", ISAKMPPolicyListView.as_view(), name="isakmppolicy_list"),
    path("isakmp_policies/add/", ISAKMPPolicyEditView.as_view(), name="isakmppolicy_creation"),
    path("isakmp_policies/delete/", ISAKMPPolicyBulkDeleteView.as_view(), name="isakmppolicy_bulk_delete"),
    path("isakmp_policies/import/", ISAKMPPolicyBulkImportView.as_view(), name="isakmppolicy_import"),
]
