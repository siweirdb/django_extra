# Generated by Django 5.0.1 on 2024-01-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]