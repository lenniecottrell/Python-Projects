# Generated by Django 3.0.8 on 2020-07-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60)),
                ('courseNumber', models.IntegerField()),
                ('instructorName', models.CharField(blank=True, max_length=60)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
