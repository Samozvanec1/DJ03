# Generated by Django 5.0.7 on 2024-08-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='Like',
            field=models.CharField(max_length=2),
        ),
    ]
