# Generated by Django 2.1.5 on 2019-02-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0019_auto_20190213_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='badge',
            name='registered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
