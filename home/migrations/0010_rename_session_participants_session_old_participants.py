# Generated by Django 4.1.12 on 2023-10-07 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0009_alter_event_start_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="session",
            old_name="participants",
            new_name="old_participants",
        ),
    ]