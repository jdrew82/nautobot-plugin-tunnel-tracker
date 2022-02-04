"""Django forms declaration for nautobot_tunnel_tracker plugin."""

from django import forms
from django.forms.models import ModelChoiceField

from nautobot.utilities.forms import forms as util_form
from nautobot.dcim.models import Device, Interface
from nautobot.extras.forms import CustomFieldModelCSVForm, DynamicModelChoiceField
from nautobot.extras.models import SecretsGroup

from .models import BaseTunnel, IKEPolicy
from .choices import (
    AuthenticationChoices,
    DHGroupChoices,
    HashChoices,
    IKEVersionChoices,
    TunnelStatusChoices,
    TunnelTypeChoices,
)

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


class IKEPolicyCreationForm(util_form.BootstrapMixin, forms.ModelForm):  # pylint: disable=no-member
    """Form for creating a new IKE policy."""

    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=100, required=False)
    version = forms.ChoiceField(choices=IKEVersionChoices.CHOICES, required=True)
    nat = forms.BooleanField(label="NAT Translation", required=False)
    authentication = forms.ChoiceField(choices=AuthenticationChoices.CHOICES, required=True)
    secrets_group = DynamicModelChoiceField(required=True, queryset=SecretsGroup.objects.all())
    hash = forms.ChoiceField(choices=HashChoices.CHOICES, required=True)
    dh_group = forms.ChoiceField(label="DH Group", choices=DHGroupChoices.CHOICES, required=True)
    pfs = forms.BooleanField(label="Perfect Forward Secrecy", required=False)

    class Meta:
        """Class to define what is used to create a new IKE policy."""

        model = IKEPolicy
        fields = [
            "name",
            "description",
            "version",
            "nat",
            "authentication",
            "hash",
            "dh_group",
            "pfs",
        ]


class IKEPolicyFilterForm(util_form.BootstrapMixin, forms.ModelForm):  # pylint: disable=no-member
    """Form for filtering IKE policy instances."""

    version = forms.ChoiceField(choices=BLANK_CHOICE + IKEVersionChoices.CHOICES, required=False)
    authentication = forms.ChoiceField(choices=BLANK_CHOICE + AuthenticationChoices.CHOICES, required=False)
    hash = forms.ChoiceField(choices=BLANK_CHOICE + HashChoices.CHOICES, required=False)
    dh_group = forms.ChoiceField(choices=BLANK_CHOICE + DHGroupChoices.CHOICES, required=False)
    pfs = forms.BooleanField(label="Perfect Forward Secrecy", required=False)
    q = forms.CharField(required=False, label="Search")

    class Meta:
        """Class to define what is used for filtering IKE policies with the search box."""

        model = IKEPolicy
        fields = [
            "version",
            "authentication",
            "hash",
            "dh_group",
            "pfs",
        ]


class IKEPolicyCreationCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import IKE policy entries."""

    class Meta:
        """Class to define what is used for bulk import of IKE policies form using CSV."""

        model = IKEPolicy
        fields = IKEPolicy.csv_headers
