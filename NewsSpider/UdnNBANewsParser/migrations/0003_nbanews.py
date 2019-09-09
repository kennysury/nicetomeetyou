# Generated by Django 2.2.5 on 2019-09-07 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UdnNBANewsParser', '0002_delete_nbanews'),
    ]

    operations = [
        migrations.CreateModel(
            name='NBANews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('content', models.CharField(max_length=65535, verbose_name='content')),
            ],
            options={
                'db_table': 'nba_news',
            },
        ),
    ]