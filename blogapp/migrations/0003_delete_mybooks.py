# Generated by Django 5.0.6 on 2024-06-17 12:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0002_mybooks"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MyBooks",
        ),
    ]
