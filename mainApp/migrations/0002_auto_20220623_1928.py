# Generated by Django 2.2 on 2022-06-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='box_creation_date',
            field=models.DateTimeField(blank=True, verbose_name='Box Date'),
        ),
        migrations.AlterField(
            model_name='boxitem',
            name='item_creation_date',
            field=models.DateTimeField(blank=True, verbose_name='Item Date'),
        ),
    ]
