# Generated by Django 4.1.5 on 2023-01-08 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='main_text',
        ),
    ]
