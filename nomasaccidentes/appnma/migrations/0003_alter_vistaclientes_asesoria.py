# Generated by Django 3.2.4 on 2022-09-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnma', '0002_auto_20220905_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vistaclientes',
            name='asesoria',
            field=models.CharField(max_length=50),
        ),
    ]