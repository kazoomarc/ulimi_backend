# Generated by Django 5.1.3 on 2024-11-22 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_finance"),
    ]

    operations = [
        migrations.CreateModel(
            name="LivestockType",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Produce",
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
                ("type", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_collected", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Livestock",
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
                ("date_of_birth", models.DateField()),
                (
                    "vaccination_status",
                    models.CharField(
                        choices=[
                            ("vaccinated", "Vaccinated"),
                            ("not_vaccinated", "Not Vaccinated"),
                            ("due", "Due for Vaccination"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="livestock",
                        to="api.livestocktype",
                    ),
                ),
            ],
        ),
    ]
