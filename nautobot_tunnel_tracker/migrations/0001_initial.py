# Generated by Django 3.1.14 on 2022-02-03 18:23

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("extras", "0021_customfield_changelog_data"),
        ("dcim", "0007_device_secrets_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseTunnel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("status", models.CharField(default="pending-configuration", max_length=30)),
                ("tunnel_type", models.CharField(default="pptp-tunnel", max_length=30)),
                ("src_device", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="dcim.device")),
                (
                    "src_interface",
                    models.OneToOneField(
                        limit_choices_to=models.Q(
                            ("app_label", "dcim"),
                            (
                                "device_name",
                                models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="dcim.device"),
                            ),
                            ("model", "interface"),
                        ),
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dcim.interface",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="IKEPolicy",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("version", models.CharField(default="ike1", max_length=100)),
                ("nat", models.BooleanField(default=False)),
                ("authentication", models.CharField(default="psk", max_length=100)),
                ("hash", models.CharField(default="hmac-md5", max_length=100)),
                ("dh_group", models.CharField(default="group1", max_length=100)),
                ("pfs", models.BooleanField(default=False)),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PPTPTunnel",
            fields=[
                (
                    "basetunnel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="nautobot_tunnel_tracker.basetunnel",
                    ),
                ),
                ("tunnel_mtu", models.IntegerField(default=1500)),
                ("clns_mtu", models.IntegerField(default=1500)),
                ("encapsulation", models.CharField(default="gre", max_length=30)),
                ("dst_device", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="dcim.device")),
                (
                    "dst_interface",
                    models.OneToOneField(
                        limit_choices_to=models.Q(
                            ("app_label", "dcim"),
                            (
                                "device_name",
                                models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="dcim.device"),
                            ),
                            ("model", "interface"),
                        ),
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dcim.interface",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
            bases=("nautobot_tunnel_tracker.basetunnel",),
        ),
    ]
