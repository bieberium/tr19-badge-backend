# Generated by Django 2.1.5 on 2019-03-05 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0022_app_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='badge.Day'),
            preserve_default=False,
        ),
    ]
