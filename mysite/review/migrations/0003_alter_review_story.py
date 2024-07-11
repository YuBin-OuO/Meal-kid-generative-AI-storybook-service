# Generated by Django 5.0.6 on 2024-07-08 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0006_delete_review"),
        ("review", "0002_remove_review_story_id_review_story_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="story",
            field=models.ForeignKey(
                default=2107,
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.readerstory",
            ),
        ),
    ]