# Generated by Django 2.2.5 on 2019-09-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UdnNBANewsParser', '0004_auto_20190907_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbanews',
            name='news_id',
            field=models.CharField(default='0000/0000000', max_length=15, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='nbanews',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]