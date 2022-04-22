# Generated by Django 3.2.10 on 2022-04-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temp_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
                ('time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
