# Generated by Django 5.0.1 on 2024-01-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatlar', '0002_rename_category_arxiv_hujjatlar_hujjatlar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arxiv_hujjatlar',
            name='file',
            field=models.FileField(upload_to='files/arxiv_hujjatlar'),
        ),
        migrations.AlterField(
            model_name='asarlar',
            name='file',
            field=models.FileField(upload_to='files/asarlar'),
        ),
        migrations.AlterField(
            model_name='dissertatsiya',
            name='file',
            field=models.FileField(upload_to='files/dissertatsiya'),
        ),
        migrations.AlterField(
            model_name='hotiralar',
            name='file',
            field=models.FileField(upload_to='files/hotiralar'),
        ),
        migrations.AlterField(
            model_name='maqolalar',
            name='file',
            field=models.FileField(upload_to='files/maqolalar'),
        ),
        migrations.AlterField(
            model_name='sherlar',
            name='file',
            field=models.FileField(upload_to='files/sherlar'),
        ),
        migrations.AlterField(
            model_name='tadqiqotlar',
            name='file',
            field=models.FileField(upload_to='files/tadqiqotlar'),
        ),
    ]