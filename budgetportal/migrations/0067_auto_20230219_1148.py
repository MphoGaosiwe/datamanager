# Generated by Django 2.2.28 on 2023-02-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgetportal", "0066_auto_20230217_1433"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="showcaseitem",
            name="button_link_1",
        ),
        migrations.RemoveField(
            model_name="showcaseitem",
            name="button_link_2",
        ),
        migrations.RemoveField(
            model_name="showcaseitem",
            name="button_text_1",
        ),
        migrations.RemoveField(
            model_name="showcaseitem",
            name="button_text_2",
        ),
        migrations.AddField(
            model_name="showcaseitem",
            name="cta_link_1",
            field=models.URLField(
                blank=True, null=True, verbose_name="Call to action link 1"
            ),
        ),
        migrations.AddField(
            model_name="showcaseitem",
            name="cta_link_2",
            field=models.URLField(
                blank=True, null=True, verbose_name="Call to action link 2"
            ),
        ),
        migrations.AddField(
            model_name="showcaseitem",
            name="cta_text_1",
            field=models.CharField(
                default="", max_length=200, verbose_name="Call to action text 1"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="showcaseitem",
            name="cta_text_2",
            field=models.CharField(
                default="", max_length=200, verbose_name="Call to action text 2"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="showcaseitem",
            name="second_cta_type",
            field=models.CharField(
                choices=[("primary", "Primary"), ("secondary", "Secondary")],
                default="primary",
                max_length=255,
                verbose_name="Second call to action type",
            ),
            preserve_default=False,
        ),
    ]
