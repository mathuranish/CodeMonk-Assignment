# Generated by Django 4.0.6 on 2022-07-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='paragraph',
            field=models.TextField(max_length=10000),
        ),
    ]
