# Generated by Django 2.2.4 on 2019-08-01 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compressor_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='dealer1_mobile',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='user_data',
            name='dealer2_mobile',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='user_data',
            name='dealer_name',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='user_data',
            name='user1_mobile',
            field=models.PositiveIntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='user_data',
            name='user2_mobile',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='user_data',
            name='user3_mobile',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compressor_data.User_Data'),
        ),
    ]