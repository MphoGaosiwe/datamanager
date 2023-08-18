# Generated by Django 2.2.10 on 2020-03-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgetportal", "0050_infraproject_sphere_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="infraproject",
            name="IRM_project_id",
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name="infraproject",
            unique_together={("sphere_slug", "IRM_project_id")},
        ),
    ]
