# Generated by Django 5.0.6 on 2024-06-25 01:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PasswordResetRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("requested_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
