# Generated by Django 4.0 on 2024-01-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutors',
            name='Xaccount',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
