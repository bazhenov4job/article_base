# Generated by Django 2.2.6 on 2019-10-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=64, unique=True, verbose_name='Источники')),
            ],
        ),
    ]
