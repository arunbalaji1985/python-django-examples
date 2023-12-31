# Generated by Django 4.2.3 on 2023-08-24 09:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('cpu', models.FloatField()),
                ('mem', models.IntegerField()),
                ('disk', models.IntegerField()),
                ('ts', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
