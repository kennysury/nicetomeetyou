# Generated by Django 2.2.5 on 2019-09-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UdnNBANewsParser', '0008_auto_20190910_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nbanews',
            name='is_new',
        ),
        migrations.AlterField(
            model_name='nbanews',
            name='content',
            field=models.TextField(max_length=4096, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='nbanews',
            name='news_id',
            field=models.CharField(default='0000_0000000', max_length=15, unique=True, verbose_name='id'),
        ),
    ]
