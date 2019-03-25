# Generated by Django 2.1.5 on 2019-03-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0023_auto_20190305_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('message', models.CharField(blank=True, editable=False, max_length=255)),
                ('sent', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='badge.Badge')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='badge.Badge')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='date',
            field=models.DateField(default='1970-01-01'),
            preserve_default=False,
        ),
    ]