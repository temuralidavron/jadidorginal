# Generated by Django 5.0.1 on 2024-01-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slayder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slayder',
            name='citations',
            field=models.IntegerField(default=0),
        ),
    ]