# Generated by Django 2.1.5 on 2019-02-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0018_auto_20190212_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='changed_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='badge',
            name='registered_at',
            field=models.DateTimeField(),
        ),
    ]