# Generated by Django 4.2.4 on 2023-08-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_friendlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="friendlist",
            name="friend_id",
            field=models.IntegerField(default=0),
        ),
    ]