# Generated by Django 2.1.5 on 2019-01-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0004_badge_registered_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='badge_id',
        ),
        migrations.AlterField(
            model_name='badge',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
