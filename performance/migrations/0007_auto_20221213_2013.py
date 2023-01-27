# Generated by Django 2.2.20 on 2022-12-13 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0006_merge_20221206_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqprsfileupload',
            name='num_imported',
            field=models.IntegerField(default=0, null=True, verbose_name='Number of rows we could import'),
        ),
        migrations.AlterField(
            model_name='eqprsfileupload',
            name='num_not_imported',
            field=models.IntegerField(default=0, null=True, verbose_name='Number of rows we could not import'),
        ),
        migrations.AlterField(
            model_name='eqprsfileupload',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='indicator',
            unique_together=set(),
        ),
    ]