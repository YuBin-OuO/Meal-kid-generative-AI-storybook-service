# Generated by Django 5.0.6 on 2024-07-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user", models.TextField(default="unknown user")),
                ("session", models.TextField(default="default session")),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("user_question", models.TextField()),
                ("chat_answer", models.TextField()),
                ("sim1", models.FloatField()),
                ("sim2", models.FloatField()),
                ("sim3", models.FloatField()),
            ],
        ),
    ]