# Generated by Django 4.2.4 on 2023-08-04 15:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0005_friendrequests"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friendrequests",
            name="user",
        ),
    ]
