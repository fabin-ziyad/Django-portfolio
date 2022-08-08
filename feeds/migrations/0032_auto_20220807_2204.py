# Generated by Django 3.2.10 on 2022-08-07 16:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0031_about_my_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='my_pic',
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='my_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='main_home'),
            preserve_default=False,
        ),
    ]