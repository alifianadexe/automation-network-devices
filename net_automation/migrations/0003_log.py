# Generated by Django 3.0.6 on 2020-05-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_automation', '0002_auto_20200505_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('time', models.DateTimeField(null=True)),
                ('messages', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
