# Generated by Django 4.2.1 on 2023-05-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_history_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="buildingType",
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name="history",
            name="condition",
            field=models.CharField(),
        ),
    ]
