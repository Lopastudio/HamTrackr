# Generated by Django 5.0.3 on 2024-03-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callsign', models.CharField(max_length=20)),
                ('frequency', models.FloatField()),
                ('mode', models.CharField(max_length=10)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
