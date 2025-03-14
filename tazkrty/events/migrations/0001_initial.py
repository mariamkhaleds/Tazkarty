# Generated by Django 4.1.13 on 2025-03-12 19:58

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('eventname', models.TextField()),
                ('eventPhoto', models.URLField()),
                ('location', models.URLField()),
                ('number_of_seats', models.IntegerField()),
                ('organizer_name', models.TextField()),
                ('status', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
    ]
