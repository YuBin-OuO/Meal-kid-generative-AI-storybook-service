# Generated by Django 5.0.6 on 2024-07-05 08:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0005_review"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Review",
        ),
    ]
