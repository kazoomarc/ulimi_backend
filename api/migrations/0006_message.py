# Generated by Django 5.1.3 on 2024-11-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_cropharvested_cropinstorage_remove_crop_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
