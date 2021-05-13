"""Django forms declaration for nautobot_tunnel_tracker plugin."""

from django import forms
from django.forms.models import ModelChoiceField

from nautobot.utilities.forms import forms as utilities_forms
from nautobot.utilities.forms.fields import DynamicModelMultipleChoiceField
from nautobot.dcim.models import Device
from nautobot.extras.forms import CustomFieldModelCSVForm

from .models import Tunnel
from .choices import TunnelStatusChoices, TunnelTypeChoices

BLANK_CHOICE = (("", "---------"),)


class TunnelCreationForm(utilities_forms.BootstrapMixin, forms.ModelForm):
    """Form for creating a new tunnel."""

    name = forms.CharField(required=True, label="Name", help_text="Name of tunnel")

    status = forms.ChoiceField(choices=BLANK_CHOICE + TunnelStatusChoices.CHOICES, required=False)

    tunnel_type = forms.ChoiceField(choices=TunnelTypeChoices.CHOICES, required=True, label="Tunnel Type")

    src_device = ModelChoiceField(
        queryset=Device.objects.all(), required=True, label="Source device", help_text="Source device for tunnel"
    )
    tunnel_mtu = forms.IntegerField(label="Tunnel MTU", help_text="MTU for tunnel")
    clns_mtu = forms.IntegerField(label="Connectionless-mode Network Service MTU", help_text="MTU for CLNS traffic")

    class Meta:
        """Class to define what is used to create a new network tunnel."""

        model = Tunnel
        fields = [
            "name",
            "status",
            "tunnel_type",
            "src_device",
            "tunnel_mtu",
            "clns_mtu",
        ]


class TunnelFilterForm(utilities_forms.BootstrapMixin, forms.ModelForm):
    """Form for filtering Tunnel instances."""

    device = forms.ModelChoiceField(queryset=Device.objects.all(), required=False)
    status = forms.ChoiceField(choices=BLANK_CHOICE + TunnelStatusChoices.CHOICES, required=False)
    q = forms.CharField(required=False, label="Search")

    class Meta:
        """Class to define what is used for filtering tunnels with the search box."""

        model = Tunnel
        fields = [
            "src_device",
            "tunnel_type",
        ]


class TunnelCreationCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import Tunnel entries."""

    class Meta:
        """Class to define what is used for bulk import of tunnels form using CSV."""

        model = Tunnel
        fields = Tunnel.csv_headers
