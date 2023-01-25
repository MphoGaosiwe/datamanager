# Generated by Django 2.2.28 on 2023-01-13 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0008_auto_20230104_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eqprsfileupload',
            name='task',
        ),
        migrations.AlterField(
            model_name='eqprsfileupload',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
