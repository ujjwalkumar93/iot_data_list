# Generated by Django 2.2.4 on 2019-08-02 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compressor_data', '0006_auto_20190802_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_detail',
            old_name='username',
            new_name='user_name_1',
        ),
        migrations.AddField(
            model_name='user_detail',
            name='user_name_2',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='user_detail',
            name='user_name_3',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='craeted_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 2, 7, 58, 37, 544078, tzinfo=utc)),
        ),
    ]
