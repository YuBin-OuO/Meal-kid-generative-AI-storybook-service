# Generated by Django 5.0.6 on 2024-07-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reader", "0004_story_keywords_story_theme"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="keywords",
            field=models.CharField(
                blank=True, default=None, max_length=1000, null=True
            ),
        ),
    ]
