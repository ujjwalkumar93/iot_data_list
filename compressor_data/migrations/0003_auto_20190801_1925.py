# Generated by Django 2.2.4 on 2019-08-01 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compressor_data', '0002_auto_20190801_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='publish_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 1, 13, 55, 25, 977892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='dealer1_mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='dealer2_mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='dealer_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='user1_mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='user2_mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='user3_mobile',
            field=models.CharField(max_length=10),
        ),
    ]
