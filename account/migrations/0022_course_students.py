# Generated by Django 3.1.2 on 2020-11-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
