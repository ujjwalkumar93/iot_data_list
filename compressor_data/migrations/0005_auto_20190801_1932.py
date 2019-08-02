# Generated by Django 2.2.4 on 2019-08-01 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compressor_data', '0004_auto_20190801_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('user1_mobile', models.CharField(max_length=10)),
                ('user2_mobile', models.CharField(max_length=10)),
                ('user3_mobile', models.CharField(max_length=10)),
                ('dealer_name', models.CharField(max_length=30)),
                ('dealer1_mobile', models.CharField(max_length=10)),
                ('dealer2_mobile', models.CharField(max_length=10)),
                ('publish_date_and_time', models.DateTimeField(default=datetime.datetime(2019, 8, 1, 14, 2, 45, 174722, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='User_Data',
        ),
    ]