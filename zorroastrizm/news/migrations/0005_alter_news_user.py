# Generated by Django 5.0.7 on 2024-08-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.CharField(blank=True, max_length=80, verbose_name='Пользователь'),
        ),
    ]