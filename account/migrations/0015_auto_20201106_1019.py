# Generated by Django 3.1.2 on 2020-11-06 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20201105_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.course')),
            ],
        ),
    ]
