# Generated by Django 5.0.6 on 2024-06-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='custom_category',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Custom Category'),
        ),
    ]
