# Generated by Django 4.1.5 on 2023-01-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
