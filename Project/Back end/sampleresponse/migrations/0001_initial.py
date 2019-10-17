# Generated by Django 2.0.5 on 2018-08-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details_1',
            fields=[
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('email', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
                ('voted', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='voters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(max_length=64, null=True)),
                ('no_of_votes', models.IntegerField(null='0')),
            ],
        ),
    ]