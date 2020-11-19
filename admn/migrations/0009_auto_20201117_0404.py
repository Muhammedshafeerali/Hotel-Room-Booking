# Generated by Django 3.1.3 on 2020-11-17 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0008_booking_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date_booked',
        ),
        migrations.AddField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default='2012-09-04'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default='2012-09-04'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admn.rooms'),
        ),
    ]
