# Generated by Django 2.2.6 on 2019-10-23 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0006_auto_20191023_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='reference_id',
            new_name='reference',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='source_id',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='theme_id',
            new_name='theme',
        ),
    ]
