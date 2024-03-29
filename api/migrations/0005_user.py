# Generated by Django 5.0.1 on 2024-02-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_category_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=120, unique=True)),
                ("name", models.CharField(max_length=120)),
                ("surname", models.CharField(max_length=120)),
                ("credit_card", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
