# Generated by Django 2.0.5 on 2018-08-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleresponse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('email', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
