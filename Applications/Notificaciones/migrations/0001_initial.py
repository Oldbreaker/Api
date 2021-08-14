# Generated by Django 3.2.6 on 2021-08-13 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('UUID', models.UUIDField()),
                ('event_type', models.CharField(max_length=50)),
                ('event_data', models.JSONField()),
            ],
        ),
    ]