# Generated by Django 3.1.2 on 2020-11-10 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20201108_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=2500)),
            ],
        ),
    ]
