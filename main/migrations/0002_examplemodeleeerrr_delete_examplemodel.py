# Generated by Django 5.0.7 on 2025-04-11 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleModeleeerrr",
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
                ("photo", models.ImageField(upload_to="photos/")),
            ],
        ),
        migrations.DeleteModel(
            name="ExampleModel",
        ),
    ]
