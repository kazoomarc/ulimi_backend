# Generated by Django 5.1.3 on 2024-11-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_livestocktype_produce_livestock"),
    ]

    operations = [
        migrations.CreateModel(
            name="CropHarvested",
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
                ("date", models.DateField()),
                (
                    "amount_harvested",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CropInStorage",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name="crop",
            name="description",
        ),
        migrations.RemoveField(
            model_name="crop",
            name="harvest_duration",
        ),
        migrations.RemoveField(
            model_name="crop",
            name="is_seasonal",
        ),
        migrations.RemoveField(
            model_name="crop",
            name="planting_date",
        ),
        migrations.AddField(
            model_name="crop",
            name="amount_planted",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="crop",
            name="date_planted",
            field=models.DateField(default="2024-01-01"),
        ),
        migrations.AddField(
            model_name="crop",
            name="expected_yield_date",
            field=models.DateField(default="2024-01-01"),
        ),
    ]