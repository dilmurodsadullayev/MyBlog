# Generated by Django 5.0.6 on 2024-06-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0004_mybooks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mybooks",
            name="stars",
            field=models.IntegerField(),
        ),
    ]
