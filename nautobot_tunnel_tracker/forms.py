"""Django forms declaration for nautobot_tunnel_tracker plugin."""

from django import forms
from django.forms.models import ModelChoiceField

from nautobot.utilities.forms import forms as util_form
from nautobot.dcim.models import Device
from nautobot.extras.forms import CustomFieldModelCSVForm, DynamicModelChoiceField

from .models import BaseTunnel
from .choices import TunnelStatusChoices, TunnelTypeChoices

BLANK_CHOICE = (("", "---------"),)


class TunnelCreationForm(util_form.BootstrapMixin, forms.ModelForm):  # pylint: disable=no-member
    """Form for creating a new tunnel."""

    status = forms.ChoiceField(choices=BLANK_CHOICE + TunnelStatusChoices.CHOICES, required=False)

    tunnel_type = forms.ChoiceField(choices=TunnelTypeChoices.CHOICES, required=True, label="Tunnel Type")

    src_device = ModelChoiceField(queryset=Device.objects.all(), required=True, label="Source Device")
    src_interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        query_params={"device_id": "$src_device"},
        required=True,
        label="Source Interface",
    )

    class Meta:
        """Class to define what is used to create a new network tunnel."""

        model = BaseTunnel
        fields = [
            "status",
            "tunnel_type",
            "src_device",
            "src_interface",
        ]


class TunnelFilterForm(util_form.BootstrapMixin, forms.ModelForm):  # pylint: disable=no-member
    """Form for filtering Tunnel instances."""

    device = forms.ModelChoiceField(queryset=Device.objects.all(), required=False)
    tunnel_type = forms.ChoiceField(choices=TunnelTypeChoices.CHOICES, required=False)
    status = forms.ChoiceField(choices=BLANK_CHOICE + TunnelStatusChoices.CHOICES, required=False)
    q = forms.CharField(required=False, label="Search")

    class Meta:
        """Class to define what is used for filtering tunnels with the search box."""

        model = BaseTunnel
        fields = [
            "device",
            "tunnel_type",
            "status",
        ]


class TunnelCreationCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import Tunnel entries."""

    class Meta:
        """Class to define what is used for bulk import of tunnels form using CSV."""

        model = BaseTunnel
        fields = BaseTunnel.csv_headers

