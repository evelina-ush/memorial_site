# Generated by Django 5.1.5 on 2025-02-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simapost',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='simapost',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
