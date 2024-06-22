# Generated by Django 5.0.6 on 2024-06-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_main', '0002_lead_custom_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='category',
            field=models.CharField(choices=[('GenAI', 'GenAI'), ('Computer Vision', 'Computer Vision'), ('Predictive Maintenance', 'Predictive Maintenance'), ('Others', 'Others')], max_length=255, verbose_name='Service Category'),
        ),
    ]