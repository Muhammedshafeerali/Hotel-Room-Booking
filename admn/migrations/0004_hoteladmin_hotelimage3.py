# Generated by Django 3.1.2 on 2020-11-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0003_auto_20201108_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteladmin',
            name='hotelimage3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
